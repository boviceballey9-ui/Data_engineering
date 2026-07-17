-- +++++++++++++++++++++++++++SQL with Data Engineering+++++++++++++++++++++++++++++ 

-- =========================Niveau 1 — Les fondamentaux============================

--  Liste tous les médicaments disponibles
SELECT * FROM Medicament;

-- Affiche toutes les ventes triées par date du plus récent au plus ancien
SELECT ID_Vente, PU, Quantite, Date FROM Ventes
ORDER BY Date DESC;

-- Affiche les médicaments dont le nom contient "cil"
SELECT IDM, Nom_Med FROM Medicament
WHERE Nom_Med LIKE '%er';

-- Affiche les achats dont le statut est NULL
SELECT ID_Achat, Date_Achat, Prix_Achat_Unit, Prix_Achat_Total, Quantite, Status 
FROM Achat_Stock
WHERE Status IS NULL;


-- =========================Niveau 2 — Agrégations et jointures============================

-- Combien de ventes a effectué chaque employé ?
SELECT e.Nom, COUNT(v.ID_Vente) AS Nbr_Ventes
FROM Employes AS e
INNER JOIN Ventes AS v
ON e.ID_Employe = v.ID_Employe
GROUP BY e.Nom
ORDER BY Nbr_Ventes DESC;

--  Quel est le chiffre d'affaires total par médicament ?
SELECT m.Nom_Med AS med, SUM(v.PU*v.Quantite) AS CA
FROM Medicament AS m
INNER JOIN ventes AS v
ON m.IDM = v.IDM
GROUP BY m.Nom_Med
ORDER BY CA DESC;

-- Affiche les ventes avec le nom du médicament et le nom de l'employé
SELECT e.nom, m.nom_med, v.Quantite, v.PU, v.Quantite*v.PU AS Total
FROM employes AS e
INNER JOIN Ventes AS v
ON e.ID_Employe = v.ID_Employe
INNER JOIN Medicament AS m
ON v.IDM = m.IDM;

-- Quels médicaments n'ont jamais été vendus ?
SELECT m.IDM, Nom_Med 
FROM Medicament AS m
LEFT JOIN Ventes AS v
ON m.IDM = v.IDM
WHERE v.IDM IS NULL;

-- Quel est le montant total des achats par médicament ?
SELECT Nom_Med, SUM(Prix_Achat_Total) AS ca_tot
FROM Medicament AS m
INNER JOIN Achat_Stock AS sa
ON sa.IDM = m.IDM
GROUP BY Nom_Med;


-- ========================= Niveau 3 — Fonctions avancées============================

--Affiche le chiffre d'affaires mensuel
SELECT DATETRUNC(month, Date) AS mois, SUM(PU*Quantite) AS ca
FROM Ventes
GROUP BY DATETRUNC(month, Date)
ORDER BY ca DESC;


--Affiche les ventes avec la saison du médicament vendu
SELECT m.Nom_Med, Saisonalite, pu, quantite, date
FROM Medicament AS m
INNER JOIN ventes AS v
ON m.IDM = v.IDM
INNER JOIN saison AS s
ON m.ID_Saison = s.ID_Saison

-- Classe les médicaments par niveau de stock avec CASE WHEN

SELECT m.nom_med, SUM(Quantite) AS Qte_total,
	CASE
		WHEN SUM(quantite) > 100 THEN 'Qte eleve'
		WHEN SUM(quantite) > 50  THEN 'Qte moyenne'
		WHEN SUM(quantite) >= 0 THEN 'Qte faible'
		ELSE 'Pas de medicaments'
	END AS Niveau_stock
FROM Medicament AS m
INNER JOIN Achat_Stock AS a
ON m.IDM = a.IDM
GROUP BY m.nom_med;

-- Affiche les ventes avec la famille thérapeutique et la catégorie
SELECT nom_med, pu, quantite, pu*quantite AS total, categorie, famille_therapeutique
FROM Ventes AS v
INNER JOIN Medicament AS m
ON m.IDM = v.IDM
INNER JOIN Categorie AS c
ON c.IDC = m.IDC
INNER JOIN Famille_therapeutique AS f
ON f.IDFT = m.IDFT;

-- Affiche les médicaments achetés cette année
SELECT nom_med, CAST(date_achat AS DATE) AS Date_achat, quantite, prix_achat_total
FROM Medicament AS m
LEFT JOIN Achat_Stock AS a
ON a.IDM = m.IDM
WHERE DATEPART(year,date_achat) = DATEPART(year, CAST(GETDATE() AS DATE));

-- ========================= Niveau 4 — CTE et Window Functions============================
--Avec une CTE, affiche le top 3 des médicaments les plus vendus
WITH medicament_vendu AS (
	SELECT nom_med, 
		SUM(quantite*pu) AS total
	FROM Medicament AS m
	INNER JOIN Ventes AS v
	ON v.IDM = m.IDM
	GROUP BY Nom_Med
	)
	SELECT TOP 3 * FROM medicament_vendu
	ORDER BY total DESC 
	;

	-- Classe les employés par chiffre d'affaires généré avec ROW_NUMBER
	WITH ca_emp AS (
		SELECT 
			e.ID_Employe,
			e.Nom,
			SUM(pu*quantite) AS total
		FROM Employes AS e
		INNER JOIN Ventes AS v
		ON v.ID_Employe = e.ID_Employe
		GROUP BY e.ID_Employe, e.Nom
		)
		SELECT 
			ROW_NUMBER() OVER (ORDER BY total DESC) AS classement,Nom, total
			FROM ca_emp;

	-- Pour chaque vente, affiche le total cumulé du chiffre d'affaires dans le temps

	SELECT 
		ID_Vente,
		Date,
		Quantite * PU                                    AS vente_du_jour,
		SUM(Quantite * PU) OVER (ORDER BY Date)          AS ca_cumule
	FROM Ventes
	ORDER BY Date;

--Compare les ventes de chaque mois avec le mois précédent (LAG)
WITH ca_mensuel AS (
	SELECT 
		DATEPART(Month, CAST(date AS Date)) AS mois, 
		SUM(Quantite * PU) AS vente_mois
	FROM Ventes 
	GROUP BY DATEPART(Month, CAST(date AS Date))
)
SELECT 
	mois, 
	vente_mois,
	LAG(vente_mois) OVER (ORDER BY mois) AS Mois_precedent,
	vente_mois - LAG(vente_mois) OVER (ORDER BY mois) AS Variance
FROM ca_mensuel;

-- Pour chaque médicament, affiche son rang de vente dans sa catégorie
WITH rank_m AS (
	SELECT nom_med, Categorie,
	SUM(pu*quantite) AS vente
	FROM Medicament AS m
	INNER JOIN Categorie AS c
	ON c.IDC = m.IDC
	INNER JOIN Ventes AS v
	ON v.IDM = m.IDM
	GROUP BY Nom_Med, Categorie
)
SELECT 
	nom_med, categorie, vente,
	RANK() OVER
		(PARTITION BY categorie
		ORDER BY vente DESC) AS rang
FROM rank_m;


-- ========================= Niveau 5 — Questions analytiques complexes============================
-- Analyse complète : marge bénéficiaire par médicament

WITH achat AS (
	SELECT IDM,
		SUM(Prix_Achat_Total) AS cout_achat
	FROM Achat_Stock
	GROUP BY IDM
),
vente AS (
	SELECT IDM,
		SUM(PU * Quantite) AS ca_vente
	FROM Ventes
	GROUP BY IDM
)
SELECT nom_med, a.cout_achat, v.ca_vente, v.ca_vente - a.cout_achat AS marge,
ROUND((v.ca_vente - a.cout_achat)/a.cout_achat * 100, 2) AS pourcentage
FROM Medicament AS m
INNER JOIN achat AS a 
ON a.IDM = m.IDM
INNER JOIN vente AS v
ON m.IDM = v.IDM
ORDER BY marge DESC;

-- Détecte les médicaments vendus mais jamais réapprovisionnés
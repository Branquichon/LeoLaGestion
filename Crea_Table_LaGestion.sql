alter table livraison drop CONSTRAINT fk_id_produit;
alter table livraison drop CONSTRAINT fk_id_fournisseur;

drop table Produit purge;
drop table Fournisseur purge;
drop table Livraison purge;


create table Produit (id_produit integer, nom_produit varchar2(30), stock_produit integer, capacite integer, avg_daily integer);
create table Fournisseur (id_fournisseur varchar2(30), nom_fournisseur varchar2(30), tel_fournisseur varchar2(30), mail_fournisseur varchar2(30));
create table Livraison (id_livraison varchar2(30), id_produit integer, id_fournisseur varchar2(30), date_livraison date, stock_entrant integer);

ALTER TABLE Produit ADD CONSTRAINT pk_Produit PRIMARY KEY (id_produit);
ALTER TABLE Livraison ADD CONSTRAINT pk_Livraison PRIMARY KEY (id_livraison);
ALTER TABLE Fournisseur ADD CONSTRAINT pk_Fournisseur PRIMARY KEY (id_fournisseur);

ALTER TABLE Livraison ADD CONSTRAINT fk_id_produit FOREIGN KEY (id_produit) REFERENCES Produit(id_produit);
ALTER TABLE Livraison ADD CONSTRAINT fk_id_fournisseur FOREIGN KEY (id_fournisseur) REFERENCES Fournisseur(id_fournisseur);



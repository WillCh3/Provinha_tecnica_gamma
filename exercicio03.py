"""3. Na programação é comum relacionar dados usando um campo que identifica
registros (id). Elabore uma modelagem de dados em que os registros estão
relacionados através de um campo identificador (o id), atendendo as seguintes
afirmações:
○ O bairro Betânia é da cidade Diamantina.
○ Os bairros Agostinho e Natal são da cidade Noronha.
○ A cidade Diamantina é do estado Goiás.
○ A cidade Noronha é do estado Paraná.
Siga o exemplo desta outra modelagem já implementada:
○ Afirmações:
■ O produto Frango é da empresa Açougue.
■ O produto Pão é da empresa Padaria.
■ O produto Leite é da empresa Padaria.
○ Modelagem resultante (os ids foram gerados aleatoriamente):
empresas = [{id:44, nome:’Açougue’},
{id:71, nome:’Padaria’}]

produtos = [{id:83, nome:’Pão’, empresa_id:71},
{id:84, nome:’Leite’, empresa_id:71},
{id:85, nome:’Frango’, empresa_id:44}]"""

#----------------------- postgres -----------------------#

CREATE TABLE "public.Empresas" (
	"id" serial NOT NULL,
	"nome" varchar(100) NOT NULL,
	CONSTRAINT "Empresas_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

CREATE TABLE "public.Produtos" (
	"id" serial NOT NULL,
	"nome" varchar(255) NOT NULL,
	"empresa_id" integer NOT NULL,
	CONSTRAINT "Produtos_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

ALTER TABLE "Produtos" ADD CONSTRAINT "Produtos_fk0" FOREIGN KEY ("empresa_id") REFERENCES "Empresas"("id");


#----------------------- mysql -----------------------#

CREATE TABLE "Empresas" (
	"id" INT NOT NULL AUTO_INCREMENT,
	"nome" varchar(100) NOT NULL,
	PRIMARY KEY ("id")
);

CREATE TABLE "Produtos" (
	"id" INT NOT NULL AUTO_INCREMENT,
	"nome" varchar(255) NOT NULL,
	"empresa_id" INT NOT NULL,
	PRIMARY KEY ("id")
);

ALTER TABLE "Produtos" ADD CONSTRAINT "Produtos_fk0" FOREIGN KEY ("empresa_id") REFERENCES "Empresas"("id");



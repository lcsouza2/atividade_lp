import sqlite3

con = sqlite3.connect('dados.db')

cur = con.cursor()

cur.execute(
    """
    CREATE TABLE professor(
        nome          VARCHAR(50)   NOT NULL,
        idade         INTEGER       NOT NULL,
        genero        VARCHAR(20)   NOT NULL,
        disciplina    VARCHAR(50)   NOT NULL,
    
    CONSTRAINT pk_professor
        PRIMARY KEY(nome, idade, genero, disciplina)
    );
    
   
    CREATE TABLE aluno(
        nome          VARCHAR(50)   NOT NULL,
        idade         INTEGER       NOT NULL,
        genero        VARCHAR(20)   NOT NULL,
        matricula     VARCHAR(25)   NOT NULL,
    
    CONSTRAINT pk_aluno
        PRIMARY KEY(matricula)
    );
    
    
    CREATE TABLE administrador(
        nome          VARCHAR(50)   NOT NULL,
        idade         INTEGER       NOT NULL,
        genero        VARCHAR(20)   NOT NULL,
        codigo        VARCHAR(10)   NOT NULL,
    
    CONSTRAINT pk_administrador
        PRIMARY KEY(codigo)
    );

    """
)

con.commit()
con.close()
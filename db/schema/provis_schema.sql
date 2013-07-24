--
-- Drop tables
--
DROP TABLE accounts_dependency_tree;
DROP TABLE hirie_account_statuses;
DROP TABLE new_hiries;
DROP TABLE teams;
DROP TABLE accounts;


--
-- Teams table
--
CREATE TABLE teams
(
    id          BIGINT NOT NULL AUTO_INCREMENT,
    team_name   VARCHAR(30) NOT NULL,
    description TEXT NULL,
    PRIMARY KEY (id),
    UNIQUE (team_name)
);

INSERT INTO teams (team_name) VALUES ('Engineering');
INSERT INTO teams (team_name) VALUES ('Sales');
INSERT INTO teams (team_name) VALUES ('Marketing');
INSERT INTO teams (team_name) VALUES ('Contractors');
COMMIT;


--
-- Accounts table
--
CREATE TABLE accounts
(
    id              BIGINT NOT NULL AUTO_INCREMENT,
    account_name    VARCHAR(30) NOT NULL,
    description     TEXT NULL,
    PRIMARY KEY (id),
    UNIQUE (account_name)
);

INSERT INTO accounts (account_name) VALUES ('Google Apps');
INSERT INTO accounts (account_name) VALUES ('One Login');
INSERT INTO accounts (account_name) VALUES ('Yammer');
COMMIT;


--
-- New Hiries table
--
CREATE TABLE new_hiries
(
    id              BIGINT          NOT NULL AUTO_INCREMENT,
    team_id         BIGINT          NOT NULL,
    first_name      VARCHAR(30)     NOT NULL,
    middle_name     VARCHAR(2)      NULL,
    last_name       VARCHAR(50)     NOT NULL,
    work_email      VARCHAR(100)    NULL,
    personal_email  VARCHAR(100)    NULL,
    signed_nda      TINYINT(1)      NOT NULL DEFAULT 0,
    early_access    TINYINT(1)      NOT NULL DEFAULT 0,
    location        VARCHAR(50)     NULL,
    notes           TEXT            NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (team_id) REFERENCES teams (id)
);


--
-- Created Accounts table
--
CREATE TABLE hirie_account_statuses
(
    id              BIGINT      NOT NULL AUTO_INCREMENT,
    new_hire_id     BIGINT      NOT NULL,
    account_id      BIGINT      NOT NULL,
    status          VARCHAR(15) NOT NULL,   -- 'Pending', 'Success', 'Failure'
    PRIMARY KEY (id),
    FOREIGN KEY (new_hire_id) REFERENCES new_hiries (id),
    FOREIGN KEY (account_id) REFERENCES accounts (id)
);


--
-- Accounts Dependencies table
--
CREATE TABLE accounts_dependency_tree
(
    id                  BIGINT      NOT NULL AUTO_INCREMENT,
    account_id          BIGINT      NOT NULL,
    parent_account_id   BIGINT      NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (account_id) REFERENCES accounts (id)
);

INSERT INTO accounts_dependency_tree (account_id, parent_account_id) VALUES ((SELECT id FROM accounts WHERE account_name = 'Google Apps'), NULL);
INSERT INTO accounts_dependency_tree (account_id, parent_account_id) VALUES ((SELECT id FROM accounts WHERE account_name = 'One Login'), (SELECT id FROM accounts WHERE account_name = 'Google Apps'));
INSERT INTO accounts_dependency_tree (account_id, parent_account_id) VALUES ((SELECT id FROM accounts WHERE account_name = 'Yammer'),    (SELECT id FROM accounts WHERE account_name = 'Google Apps'));
COMMIT;

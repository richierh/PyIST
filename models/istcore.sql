--
-- File generated with SQLiteStudio v3.2.1 on Min Jan 12 18:21:37 2020
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Data Peserta
CREATE TABLE "Data Peserta" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"no tes"	INTEGER,
	"nama"	TEXT,
	"jenis kelamin"	TEXT,
	"tanggal lahir"	TEXT,
	"usia"	TEXT,
	"asal sekolah"	TEXT,
	"pendidikan terakhir"	TEXT,
	"jurusan"	TEXT,
	"posisi pekerjaan"	TEXT,
	"perusahaan"	TEXT,
	"TipeNormaID"	INTEGER,
	FOREIGN KEY("TipeNormaID") REFERENCES "Tipe Norma"("TipeNormaID")
);
INSERT INTO "Data Peserta" (id, "no tes", nama, "jenis kelamin", "tanggal lahir", usia, "asal sekolah", "pendidikan terakhir", jurusan, "posisi pekerjaan", perusahaan, TipeNormaID) VALUES (1, 1, 'Suaeb', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1);

-- Table: Input Jawaban
CREATE TABLE "Input Jawaban" ("id manual" INTEGER PRIMARY KEY ASC AUTOINCREMENT, SE INT, WA INT, AN INT, GE INT, RA INT, ZR INT, FA INT, WU INT, ME INT, TipeInputId INTEGER, id INTEGER, FOREIGN KEY (id) REFERENCES "Data Peserta" (id), FOREIGN KEY (TipeInputId) REFERENCES "Tipe Input" (TipeInputId));
INSERT INTO "Input Jawaban" ("id manual", SE, WA, AN, GE, RA, ZR, FA, WU, ME, TipeInputId, id) VALUES (1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, 1);

-- Table: Jawaban Norma
CREATE TABLE "Jawaban Norma" (JawabanNormaID INTEGER PRIMARY KEY AUTOINCREMENT, id INTEGER, FOREIGN KEY (id) REFERENCES "Data Peserta" (id));

-- Table: Jenis Norma
CREATE TABLE "Jenis Norma" (NormaID INTEGER PRIMARY KEY AUTOINCREMENT, "Jenis Norma" TEXT, Keterangan TEXT, TipeNormaID INTEGER, FOREIGN KEY (TipeNormaID) REFERENCES "Tipe Norma" (TipeNormaID));
INSERT INTO "Jenis Norma" (NormaID, "Jenis Norma", Keterangan, TipeNormaID) VALUES (1, 'Norma Pendidikan', NULL, 1);
INSERT INTO "Jenis Norma" (NormaID, "Jenis Norma", Keterangan, TipeNormaID) VALUES (2, 'Norma Pekerjaan', 'tess', 1);
INSERT INTO "Jenis Norma" (NormaID, "Jenis Norma", Keterangan, TipeNormaID) VALUES (3, 'Norma Sendiri', 'None', 2);

-- Table: jumlah
CREATE TABLE "jumlah" (
	"RS"	VARCHAR,
	"SW"	INTEGER
);
INSERT INTO jumlah (RS, SW) VALUES ('25-26', 70);
INSERT INTO jumlah (RS, SW) VALUES ('27-28', 71);
INSERT INTO jumlah (RS, SW) VALUES ('29-30', 72);
INSERT INTO jumlah (RS, SW) VALUES ('31-32', 73);
INSERT INTO jumlah (RS, SW) VALUES ('33-34', 74);
INSERT INTO jumlah (RS, SW) VALUES ('35-36', 75);
INSERT INTO jumlah (RS, SW) VALUES ('37-38', 76);
INSERT INTO jumlah (RS, SW) VALUES ('39-40', 77);
INSERT INTO jumlah (RS, SW) VALUES ('41-42', 78);
INSERT INTO jumlah (RS, SW) VALUES ('43-44', 79);
INSERT INTO jumlah (RS, SW) VALUES ('45-46', 80);
INSERT INTO jumlah (RS, SW) VALUES ('47-48', 81);
INSERT INTO jumlah (RS, SW) VALUES ('49-50', 82);
INSERT INTO jumlah (RS, SW) VALUES ('51-52', 83);
INSERT INTO jumlah (RS, SW) VALUES ('53-54', 84);
INSERT INTO jumlah (RS, SW) VALUES ('55-57', 85);
INSERT INTO jumlah (RS, SW) VALUES ('58-59', 86);
INSERT INTO jumlah (RS, SW) VALUES ('60-61', 87);
INSERT INTO jumlah (RS, SW) VALUES ('62-63', 88);
INSERT INTO jumlah (RS, SW) VALUES ('64-65', 89);
INSERT INTO jumlah (RS, SW) VALUES ('66-67', 90);
INSERT INTO jumlah (RS, SW) VALUES ('68-69', 91);
INSERT INTO jumlah (RS, SW) VALUES ('70-71', 92);
INSERT INTO jumlah (RS, SW) VALUES ('72-73', 93);
INSERT INTO jumlah (RS, SW) VALUES ('74-75', 94);
INSERT INTO jumlah (RS, SW) VALUES ('76-77', 95);
INSERT INTO jumlah (RS, SW) VALUES ('78-79', 96);
INSERT INTO jumlah (RS, SW) VALUES ('80', 97);
INSERT INTO jumlah (RS, SW) VALUES ('81-83', 98);
INSERT INTO jumlah (RS, SW) VALUES ('84-85', 99);
INSERT INTO jumlah (RS, SW) VALUES ('86-87', 100);
INSERT INTO jumlah (RS, SW) VALUES ('88-89', 101);
INSERT INTO jumlah (RS, SW) VALUES ('90-91', 102);
INSERT INTO jumlah (RS, SW) VALUES ('92-93', 103);
INSERT INTO jumlah (RS, SW) VALUES ('94-95', 104);
INSERT INTO jumlah (RS, SW) VALUES ('96-97', 105);
INSERT INTO jumlah (RS, SW) VALUES ('98-99', 106);
INSERT INTO jumlah (RS, SW) VALUES ('100-101', 107);
INSERT INTO jumlah (RS, SW) VALUES ('102-103', 108);
INSERT INTO jumlah (RS, SW) VALUES ('104-105', 109);
INSERT INTO jumlah (RS, SW) VALUES ('106-107', 110);
INSERT INTO jumlah (RS, SW) VALUES ('108-109', 111);
INSERT INTO jumlah (RS, SW) VALUES ('110-111', 112);
INSERT INTO jumlah (RS, SW) VALUES ('112-113', 113);
INSERT INTO jumlah (RS, SW) VALUES ('114-115', 114);
INSERT INTO jumlah (RS, SW) VALUES ('116-117', 115);
INSERT INTO jumlah (RS, SW) VALUES ('118-119', 116);
INSERT INTO jumlah (RS, SW) VALUES ('120-121', 117);
INSERT INTO jumlah (RS, SW) VALUES ('122-124', 118);
INSERT INTO jumlah (RS, SW) VALUES ('125-126', 119);
INSERT INTO jumlah (RS, SW) VALUES ('127-128', 120);
INSERT INTO jumlah (RS, SW) VALUES ('129-130', 121);
INSERT INTO jumlah (RS, SW) VALUES ('131-132', 122);
INSERT INTO jumlah (RS, SW) VALUES ('133-134', 123);
INSERT INTO jumlah (RS, SW) VALUES ('135-136', 124);
INSERT INTO jumlah (RS, SW) VALUES ('137-138', 125);
INSERT INTO jumlah (RS, SW) VALUES ('139-140', 126);
INSERT INTO jumlah (RS, SW) VALUES ('141-142', 127);
INSERT INTO jumlah (RS, SW) VALUES ('143-144', 128);
INSERT INTO jumlah (RS, SW) VALUES ('145-146', 129);
INSERT INTO jumlah (RS, SW) VALUES ('147-148', 130);
INSERT INTO jumlah (RS, SW) VALUES ('149-150', 131);
INSERT INTO jumlah (RS, SW) VALUES ('151-152', 132);

-- Table: Konversi GE
CREATE TABLE "Konversi GE" (idGE INTEGER PRIMARY KEY AUTOINCREMENT, "No" TEXT, RW TEXT, GE TEXT);

-- Table: Norma
CREATE TABLE Norma (IdNorma INTEGER PRIMARY KEY AUTOINCREMENT, "Nama Norma" TEXT, Keterangan TEXT, NormaID TEXT, FOREIGN KEY (NormaID) REFERENCES "Jenis Norma" (NormaID));
INSERT INTO Norma (IdNorma, "Nama Norma", Keterangan, NormaID) VALUES (17, 'sadf', 'dhdhfdghh', '3');
INSERT INTO Norma (IdNorma, "Nama Norma", Keterangan, NormaID) VALUES (19, 'xcv', 'vnbvcb', '3');
INSERT INTO Norma (IdNorma, "Nama Norma", Keterangan, NormaID) VALUES (20, 'sdf', 'sgsg', '3');
INSERT INTO Norma (IdNorma, "Nama Norma", Keterangan, NormaID) VALUES (21, 'cxvxz', '', '3');
INSERT INTO Norma (IdNorma, "Nama Norma", Keterangan, NormaID) VALUES (22, 'asdf', '', '3');
INSERT INTO Norma (IdNorma, "Nama Norma", Keterangan, NormaID) VALUES (23, 'asdf', '', '3');
INSERT INTO Norma (IdNorma, "Nama Norma", Keterangan, NormaID) VALUES (24, 'asdf', '', '3');
INSERT INTO Norma (IdNorma, "Nama Norma", Keterangan, NormaID) VALUES (25, 'sdf', '', '3');
INSERT INTO Norma (IdNorma, "Nama Norma", Keterangan, NormaID) VALUES (26, 'asdf', 'sadfsaf', '3');
INSERT INTO Norma (IdNorma, "Nama Norma", Keterangan, NormaID) VALUES (27, 'sdf', '', '3');
INSERT INTO Norma (IdNorma, "Nama Norma", Keterangan, NormaID) VALUES (28, 'fsaf', '', '3');
INSERT INTO Norma (IdNorma, "Nama Norma", Keterangan, NormaID) VALUES (29, 'sdfg', '', '3');
INSERT INTO Norma (IdNorma, "Nama Norma", Keterangan, NormaID) VALUES (30, 'asd', '', '3');

-- Table: NORMA IST IQ
CREATE TABLE "NORMA IST IQ" (SW INTEGER, IQ INTEGER, "%" INTEGER);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (140, 160, 100);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (138, 157, 100);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (136, 154, 100);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (134, 151, 100);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (132, 145, 100);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (129, 143, 100);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (128, 142, 100);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (127, 140, 100);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (126, 139, 100);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (125, 137, 99);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (124, 136, 99);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (123, 134, 99);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (122, 133, 99);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (121, 131, 98);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (120, 130, 98);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (119, 128, 97);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (118, 127, 96);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (117, 125, 95);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (116, 124, 95);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (115, 122, 93);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (114, 121, 92);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (113, 120, 90);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (112, 118, 88);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (111, 116, 86);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (110, 115, 84);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (109, 113, 81);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (108, 112, 79);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (107, 110, 76);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (106, 109, 73);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (105, 107, 70);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (104, 106, 66);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (103, 104, 62);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (102, 103, 58);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (101, 101, 54);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (100, 100, 50);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (99, 98, 46);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (98, 97, 42);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (97, 96, 38);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (96, 94, 34);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (95, 92, 30);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (94, 91, 27);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (93, 90, 24);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (92, 88, 21);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (91, 87, 18);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (90, 85, 15);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (89, 84, 14);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (88, 82, 12);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (87, 81, 10);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (86, 79, 8);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (85, 78, 7);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (84, 76, 5);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (83, 75, 4);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (82, 73, 3);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (81, 71, 2);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (80, 70, 2);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (79, 68, 1);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (78, 67, 1);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (77, 66, 1);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (76, 64, 1);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (75, 62, 0);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (74, 61, 0);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (73, 59, 0);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (72, 58, 0);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (70, 55, 0);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (68, 52, 0);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (66, 49, 0);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (64, 46, 0);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (62, 43, 0);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (60, 40, 0);
INSERT INTO "NORMA IST IQ" (SW, IQ, "%") VALUES (58, 37, 0);

-- Table: Norma Pendidikan
CREATE TABLE "Norma Pendidikan" (NormaPendidikanID INTEGER PRIMARY KEY AUTOINCREMENT, Usia INT, "Nama Norma" TEXT, Keterangan TEXT, NormaID INTEGER, FOREIGN KEY (NormaID) REFERENCES "Jenis Norma" (NormaID));
INSERT INTO "Norma Pendidikan" (NormaPendidikanID, Usia, "Nama Norma", Keterangan, NormaID) VALUES (1, 12, 'Norma Usia 12 Tahun', 'Keterangandfsdf', 1);
INSERT INTO "Norma Pendidikan" (NormaPendidikanID, Usia, "Nama Norma", Keterangan, NormaID) VALUES (2, 13, 'Norma Usia 13 Tahun', 'tess', 1);
INSERT INTO "Norma Pendidikan" (NormaPendidikanID, Usia, "Nama Norma", Keterangan, NormaID) VALUES (3, 14, 'Norma Usia 14 Tahun', 'None', 1);
INSERT INTO "Norma Pendidikan" (NormaPendidikanID, Usia, "Nama Norma", Keterangan, NormaID) VALUES (4, 15, 'Norma Usia 15 Tahun', 'None', 1);
INSERT INTO "Norma Pendidikan" (NormaPendidikanID, Usia, "Nama Norma", Keterangan, NormaID) VALUES (5, 16, 'Norma Usia 16 Tahun', 'None', 1);
INSERT INTO "Norma Pendidikan" (NormaPendidikanID, Usia, "Nama Norma", Keterangan, NormaID) VALUES (6, 17, 'Norma Usia 17 Tahun', 'None', 1);
INSERT INTO "Norma Pendidikan" (NormaPendidikanID, Usia, "Nama Norma", Keterangan, NormaID) VALUES (7, 18, 'Norma Usia 18 Tahun', 'None', 1);
INSERT INTO "Norma Pendidikan" (NormaPendidikanID, Usia, "Nama Norma", Keterangan, NormaID) VALUES (8, 19, 'Norma Usia 19 Tahun', 'None', 1);

-- Table: NormaISTSMA,D3,S1
CREATE TABLE "NormaISTSMA,D3,S1" (RS INTEGER, "01 SE" INTEGER, "02 WA" INTEGER, "03 AN" INTEGER, "04 GE" INTEGER, "05 RA" INTEGER, "06 ZR" INTEGER, "07 FA" INTEGER, "08 WU" INTEGER, "09 ME" INTEGER);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (0, 71, 67, 79, 70, 79, 85, 69, 75, 74);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (1, 75, 71, 83, 72, 82, 87, 73, 78, 76);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (2, 78, 74, 86, 75, 84, 89, 75, 81, 78);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (3, 82, 78, 89, 77, 87, 91, 79, 84, 80);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (4, 86, 81, 92, 79, 89, 93, 82, 87, 82);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (5, 90, 84, 96, 81, 92, 95, 85, 90, 84);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (6, 93, 88, 99, 84, 95, 96, 88, 93, 87);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (7, 97, 92, 102, 86, 97, 98, 91, 96, 89);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (8, 101, 95, 106, 88, 100, 100, 94, 99, 91);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (9, 105, 98, 109, 90, 102, 102, 97, 102, 93);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (10, 108, 102, 112, 93, 105, 104, 100, 105, 95);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (11, 112, 105, 115, 95, 107, 104, 103, 108, 98);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (12, 116, 109, 119, 97, 110, 108, 104, 111, 100);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (13, 120, 112, 122, 99, 112, 109, 109, 114, 102);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (14, 123, 116, 125, 101, 115, 111, 112, 117, 104);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (15, 127, 119, 129, 104, 118, 113, 115, 120, 106);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (16, 131, 123, 132, 106, 120, 115, 118, 123, 108);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (17, 135, 125, 135, 108, 123, 117, 121, 126, 110);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (18, 138, 130, 138, 110, 125, 119, 124, 129, 115);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (19, 142, 133, 142, 113, 128, 121, 127, 131, 116);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (20, 146, 137, 145, 115, 130, 122, 130, 134, 117);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (21, NULL, NULL, NULL, 117, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (22, NULL, NULL, NULL, 119, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (23, NULL, NULL, NULL, 122, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (24, NULL, NULL, NULL, 124, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (25, NULL, NULL, NULL, 126, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (26, NULL, NULL, NULL, 128, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (27, NULL, NULL, NULL, 131, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (28, NULL, NULL, NULL, 133, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (29, NULL, NULL, NULL, 135, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (30, NULL, NULL, NULL, 137, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (31, NULL, NULL, NULL, 140, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "NormaISTSMA,D3,S1" (RS, "01 SE", "02 WA", "03 AN", "04 GE", "05 RA", "06 ZR", "07 FA", "08 WU", "09 ME") VALUES (32, NULL, NULL, NULL, 142, NULL, NULL, NULL, NULL, NULL);

-- Table: NormaSarjana
CREATE TABLE NormaSarjana (Norma INTEGER, SE INTEGER, WA INTEGER, AN INTEGER, GE INTEGER, ME INTEGER, RA INTEGER, ZR INTEGER, FA INTEGER, WU INTEGER, TOTAL INTEGER, Ket INTEGER);
INSERT INTO NormaSarjana (Norma, SE, WA, AN, GE, ME, RA, ZR, FA, WU, TOTAL, Ket) VALUES (5, '136<', '122<', '166<', '126<', '137<', '133<', '137<', '126<', '132<', '127<', 'Superior');
INSERT INTO NormaSarjana (Norma, SE, WA, AN, GE, ME, RA, ZR, FA, WU, TOTAL, Ket) VALUES (4, '122-135', '109-121', '137-165', '114-125', '118-136', '116-132', '119-136', '110-125', '114-131', '117-126', 'Diatas rata-rata');
INSERT INTO NormaSarjana (Norma, SE, WA, AN, GE, ME, RA, ZR, FA, WU, TOTAL, Ket) VALUES (3, '108-121', '97-108', '108-136', '103-113', '100-117', '100-115', '101-118', '93-109', '96-113', '107-116', 'Rata-rata atas');
INSERT INTO NormaSarjana (Norma, SE, WA, AN, GE, ME, RA, ZR, FA, WU, TOTAL, Ket) VALUES (2, '95-107', '84-96', '79-107', '91-102', '82-99', '83-99', '84-100', '77-92', '78-95', '97-106', 'Rata-rata');
INSERT INTO NormaSarjana (Norma, SE, WA, AN, GE, ME, RA, ZR, FA, WU, TOTAL, Ket) VALUES (1, '<94', ',<83', '<78', '<90', '<81', '<82', '<83', '<76', '<77', '<96', 'Rata-rata bawah');

-- Table: NormaSendiri
CREATE TABLE NormaSendiri ("No" INT, RS INT, SE INT, WA INT, AN INT, GE INT, RA INT, ZE INT, FA INT, WU INT, ME INT, IdNorma INT, FOREIGN KEY (IdNorma) REFERENCES Norma (IdNorma) ON DELETE SET DEFAULT);

-- Table: NormaSLTA/STM
CREATE TABLE "NormaSLTA/STM" (Norma VARCHAR, SE VARCHAR, AN VARCHAR, GE VARCHAR, WA VARCHAR, ME VARCHAR, RA VARCHAR, ZR VARCHAR, FA VARCHAR, WU VARCHAR, TOTAL VARCHAR, Ket VARCHAR);
INSERT INTO "NormaSLTA/STM" (Norma, SE, AN, GE, WA, ME, RA, ZR, FA, WU, TOTAL, Ket) VALUES ('5', '113<', '117<', '118<', '118<', '108<', '114<', '119<', '114<', '119<', '116<', 'Superior');
INSERT INTO "NormaSLTA/STM" (Norma, SE, AN, GE, WA, ME, RA, ZR, FA, WU, TOTAL, Ket) VALUES ('4', '105-112', '137-165', '109-116', '109-117', '99-107', '104-113', '110-118', '106-113', '109-118', '107-115', 'Diatas rata-rata');
INSERT INTO "NormaSLTA/STM" (Norma, SE, AN, GE, WA, ME, RA, ZR, FA, WU, TOTAL, Ket) VALUES ('3', '94-104', '101-108', '97-106', '100-108', '90-98', '95-103', '103-109', '99-105', '100-108', '97-106', 'Rata-rata atas');
INSERT INTO "NormaSLTA/STM" (Norma, SE, AN, GE, WA, ME, RA, ZR, FA, WU, TOTAL, Ket) VALUES ('2', '88-96', '93-100', '86-96', '91-99', '81-89', '86-94', '95-102', '92-98', '90-99', '87-96', 'Rata-rata');
INSERT INTO "NormaSLTA/STM" (Norma, SE, AN, GE, WA, ME, RA, ZR, FA, WU, TOTAL, Ket) VALUES ('1', '<87', '<92', '<85', '<90', '<80', '<85', '<94', '<91', '<89', '<86', 'Rata-rata bawah');

-- Table: Tipe Input
CREATE TABLE "Tipe Input" (TipeInputId INTEGER PRIMARY KEY AUTOINCREMENT, "Jenis Input" TEXT);
INSERT INTO "Tipe Input" (TipeInputId, "Jenis Input") VALUES (1, 'Input Manual');
INSERT INTO "Tipe Input" (TipeInputId, "Jenis Input") VALUES (2, 'Input Total');

-- Table: Tipe Norma
CREATE TABLE "Tipe Norma" (TipeNormaID INTEGER PRIMARY KEY AUTOINCREMENT, "Jenis Norma" TEXT);
INSERT INTO "Tipe Norma" (TipeNormaID, "Jenis Norma") VALUES (1, 'Tetap');
INSERT INTO "Tipe Norma" (TipeNormaID, "Jenis Norma") VALUES (2, 'Tidak Tetap');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

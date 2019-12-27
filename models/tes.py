# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class KonversiGE(Base):
    __tablename__ = 'Konversi GE'

    idGE = Column(Integer, primary_key=True)
    No = Column(Text)
    RW = Column(Text)
    GE = Column(Text)


t_NORMA IST IQ = Table(
    'NORMA IST IQ', metadata,
    Column('SW', Integer),
    Column('IQ', Integer),
    Column('%', Integer)
)


t_NormaISTSMA,D3,S1 = Table(
    'NormaISTSMA,D3,S1', metadata,
    Column('RS', Integer),
    Column('01 SE', Integer),
    Column('02 WA', Integer),
    Column('03 AN', Integer),
    Column('04 GE', Integer),
    Column('05 RA', Integer),
    Column('06 ZR', Integer),
    Column('07 FA', Integer),
    Column('08 WU', Integer),
    Column('09 ME', Integer)
)


t_NormaSLTA/STM = Table(
    'NormaSLTA/STM', metadata,
    Column('Norma', String),
    Column('SE', String),
    Column('AN', String),
    Column('GE', String),
    Column('WA', String),
    Column('ME', String),
    Column('RA', String),
    Column('ZR', String),
    Column('FA', String),
    Column('WU', String),
    Column('TOTAL', String),
    Column('Ket', String)
)


t_NormaSarjana = Table(
    'NormaSarjana', metadata,
    Column('Norma', Integer),
    Column('SE', Integer),
    Column('WA', Integer),
    Column('AN', Integer),
    Column('GE', Integer),
    Column('ME', Integer),
    Column('RA', Integer),
    Column('ZR', Integer),
    Column('FA', Integer),
    Column('WU', Integer),
    Column('TOTAL', Integer),
    Column('Ket', Integer)
)


class TipeInput(Base):
    __tablename__ = 'Tipe Input'

    TipeInputId = Column(Integer, primary_key=True)
    Jenis_Input = Column('Jenis Input', Text)


class TipeNorma(Base):
    __tablename__ = 'Tipe Norma'

    TipeNormaID = Column(Integer, primary_key=True)
    Jenis_Norma = Column('Jenis Norma', Text)


t_jumlah = Table(
    'jumlah', metadata,
    Column('RS', String),
    Column('SW', Integer)
)


t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)


t_sqlite_stat1 = Table(
    'sqlite_stat1', metadata,
    Column('tbl', NullType),
    Column('idx', NullType),
    Column('stat', NullType)
)


t_sqlite_stat4 = Table(
    'sqlite_stat4', metadata,
    Column('tbl', NullType),
    Column('idx', NullType),
    Column('neq', NullType),
    Column('nlt', NullType),
    Column('ndlt', NullType),
    Column('sample', NullType)
)


class DataPeserta(Base):
    __tablename__ = 'Data Peserta'

    id = Column(Integer, primary_key=True)
    no_tes = Column('no tes', Integer)
    nama = Column(Text)
    jenis_kelamin = Column('jenis kelamin', Text)
    tanggal_lahir = Column('tanggal lahir', Text)
    usia = Column(Text)
    asal_sekolah = Column('asal sekolah', Text)
    pendidikan_terakhir = Column('pendidikan terakhir', Text)
    jurusan = Column(Text)
    posisi_pekerjaan = Column('posisi pekerjaan', Text)
    perusahaan = Column(Text)
    TipeNormaID = Column(ForeignKey('Tipe Norma.TipeNormaID'))

    Tipe_Norma = relationship('TipeNorma')


class JenisNorma(Base):
    __tablename__ = 'Jenis Norma'

    NormaID = Column(Integer, primary_key=True)
    Jenis_Norma = Column('Jenis Norma', Text)
    Keterangan = Column(Text)
    TipeNormaID = Column(ForeignKey('Tipe Norma.TipeNormaID'))

    Tipe_Norma = relationship('TipeNorma')


class InputJawaban(Base):
    __tablename__ = 'Input Jawaban'

    id_manual = Column('id manual', Integer, primary_key=True)
    SE = Column(Integer)
    WA = Column(Integer)
    AN = Column(Integer)
    GE = Column(Integer)
    RA = Column(Integer)
    ZR = Column(Integer)
    FA = Column(Integer)
    WU = Column(Integer)
    ME = Column(Integer)
    TipeInputId = Column(ForeignKey('Tipe Input.TipeInputId'))
    id = Column(ForeignKey('Data Peserta.id'))

    Tipe_Input = relationship('TipeInput')
    Data_Peserta = relationship('DataPeserta')


class JawabanNorma(Base):
    __tablename__ = 'Jawaban Norma'

    JawabanNormaID = Column(Integer, primary_key=True)
    id = Column(ForeignKey('Data Peserta.id'))

    Data_Peserta = relationship('DataPeserta')


class Norma(Base):
    __tablename__ = 'Norma'

    IdNorma = Column(Integer, primary_key=True)
    Nama_Norma = Column('Nama Norma', Text)
    NormaID = Column(ForeignKey('Jenis Norma.NormaID'))

    Jenis_Norma = relationship('JenisNorma')


class NormaPendidikan(Base):
    __tablename__ = 'Norma Pendidikan'

    NormaPendidikanID = Column(Integer, primary_key=True)
    Usia = Column(Integer)
    Nama_Norma = Column('Nama Norma', Text)
    Keterangan = Column(Text)
    NormaID = Column(ForeignKey('Jenis Norma.NormaID'))

    Jenis_Norma = relationship('JenisNorma')

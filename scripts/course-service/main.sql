-- author: Norman Aberin
-- version: v1.0.1
--
-- the following tables are the initial simplified
-- version of the database tables

-------------------------------------------------
-- create table statements
-------------------------------------------------
CREATE TABLE OC_CATEGORIES (
    CATEGORY_ID            number generated by default on null as identity
        primary key,
    CATEGORY               varchar2(255),
    CONSTRAINT uq_category_name unique(CATEGORY)
);

CREATE TABLE OC_COURSES (
    COURSE_ID               number generated by default on null as identity
        primary key,
    COURSE_NAME             varchar2(255) not null,
    COURSE_DESCRIPTION      varchar2(4000) not null,
    COURSE_IMG_LINK         varchar2(4000),
    IS_ACTIVE               number not null check(IS_ACTIVE in (0, 1)),
    CATEGORY_ID             number not null references OC_CATEGORIES(CATEGORY_ID)
);

CREATE TABLE OC_LESSON_SECTIONS (
    LESSON_SECTION_ID       number generated by default on null as identity
        primary key,
    LESSON_SECTION_NAME     varchar2(255) not null,
    LESSON_SECTION_ORDER    number,
    COURSE_ID               number not null references OC_COURSES(COURSE_ID) on delete cascade
);

CREATE TABLE OC_LESSONS (
    LESSON_ID               number generated by default on null as identity
        primary key,
    LESSON_NAME             varchar2(255) not null,
    LESSON_DESCRIPTION      varchar2(255),
    SECTION_ID              number not null
        references OC_LESSON_SECTIONS(LESSON_SECTION_ID) on delete cascade,
    LESSON_ORDER            number not null

);

CREATE TABLE OC_TAGS (
    TAG_ID                  number generated by default on null as identity
        primary key,
    TAG                     varchar2(255),
    CONSTRAINT uq_tag unique(TAG)
);

CREATE TABLE OC_COURSE_TAGS (
    SUB_ID                  number generated by default on null as identity
        primary key,
    TAG_ID                  number not null
        references OC_TAGS(TAG_ID),
    COURSE_ID               number not null
        references OC_COURSES(COURSE_ID) on delete cascade,
    CONSTRAINT uq_course_tag UNIQUE (TAG_ID, COURSE_ID)
);

-------------------------------------------------
-- insert statements
-------------------------------------------------
insert into OC_CATEGORIES(CATEGORY)
with categories as (
    select 'Software' cat from dual union all
    select 'Business' cat from dual union all
    select 'STEM' cat from dual union all
    select 'Health Science' cat from dual union all
    select 'Finance & Accounting' cat  from dual union all
    select 'Design' cat from dual union all
    select 'Music' cat from dual union all
    select 'Sports' cat from dual
) select * from categories;


insert into OC_TAGS(TAG)
with tags as (
    select 'Java' tag from dual union all
    select 'JavaScript' tag from dual union all
    select 'Python' tag from dual union all
    select 'Go' tag from dual union all
    select 'Machine Learning' tag from dual union all
    select 'Google Cloud' tag from dual union all
    select 'Oracle Cloud' tag from dual union all
    select 'Databases' tag from dual union all
    select 'Apache Spark' tag from dual union all
    select 'Data Structures and Algorithms' tag from dual union all
    select 'Chemistry' tag from dual
) select * from tags;


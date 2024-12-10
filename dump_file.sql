--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: brand
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO brand;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: brand
--

COMMENT ON SCHEMA public IS '';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: User; Type: TABLE; Schema: public; Owner: brand
--

CREATE TABLE public."User" (
    id integer NOT NULL,
    email text NOT NULL,
    name text NOT NULL,
    image text NOT NULL,
    "favoritePet" text,
    "createdAt" timestamp(3) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    "updatedAt" timestamp(3) without time zone NOT NULL,
    provider text,
    "providerAccountId" text
);


ALTER TABLE public."User" OWNER TO brand;

--
-- Name: User_id_seq; Type: SEQUENCE; Schema: public; Owner: brand
--

CREATE SEQUENCE public."User_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."User_id_seq" OWNER TO brand;

--
-- Name: User_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: brand
--

ALTER SEQUENCE public."User_id_seq" OWNED BY public."User".id;


--
-- Name: _prisma_migrations; Type: TABLE; Schema: public; Owner: brand
--

CREATE TABLE public._prisma_migrations (
    id character varying(36) NOT NULL,
    checksum character varying(64) NOT NULL,
    finished_at timestamp with time zone,
    migration_name character varying(255) NOT NULL,
    logs text,
    rolled_back_at timestamp with time zone,
    started_at timestamp with time zone DEFAULT now() NOT NULL,
    applied_steps_count integer DEFAULT 0 NOT NULL
);


ALTER TABLE public._prisma_migrations OWNER TO brand;

--
-- Name: crimes; Type: TABLE; Schema: public; Owner: brand
--

CREATE TABLE public.crimes (
    crime_id integer NOT NULL,
    type text,
    description text,
    location text,
    date_reported date
);


ALTER TABLE public.crimes OWNER TO brand;

--
-- Name: crimes_crime_id_seq; Type: SEQUENCE; Schema: public; Owner: brand
--

CREATE SEQUENCE public.crimes_crime_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.crimes_crime_id_seq OWNER TO brand;

--
-- Name: crimes_crime_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: brand
--

ALTER SEQUENCE public.crimes_crime_id_seq OWNED BY public.crimes.crime_id;


--
-- Name: houses; Type: TABLE; Schema: public; Owner: brand
--

CREATE TABLE public.houses (
    zpid integer NOT NULL,
    address character varying(255) NOT NULL,
    price numeric NOT NULL,
    lat double precision,
    long double precision
);


ALTER TABLE public.houses OWNER TO brand;

--
-- Name: houses_zpid_seq; Type: SEQUENCE; Schema: public; Owner: brand
--

CREATE SEQUENCE public.houses_zpid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.houses_zpid_seq OWNER TO brand;

--
-- Name: houses_zpid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: brand
--

ALTER SEQUENCE public.houses_zpid_seq OWNED BY public.houses.zpid;


--
-- Name: schools; Type: TABLE; Schema: public; Owner: brand
--

CREATE TABLE public.schools (
    name character varying(200) NOT NULL,
    grades character varying(25),
    rating integer
);


ALTER TABLE public.schools OWNER TO brand;

--
-- Name: users; Type: TABLE; Schema: public; Owner: brand
--

CREATE TABLE public.users (
    account text NOT NULL,
    first_name text,
    last_name text,
    created_on date
);


ALTER TABLE public.users OWNER TO brand;

--
-- Name: User id; Type: DEFAULT; Schema: public; Owner: brand
--

ALTER TABLE ONLY public."User" ALTER COLUMN id SET DEFAULT nextval('public."User_id_seq"'::regclass);


--
-- Name: crimes crime_id; Type: DEFAULT; Schema: public; Owner: brand
--

ALTER TABLE ONLY public.crimes ALTER COLUMN crime_id SET DEFAULT nextval('public.crimes_crime_id_seq'::regclass);


--
-- Name: houses zpid; Type: DEFAULT; Schema: public; Owner: brand
--

ALTER TABLE ONLY public.houses ALTER COLUMN zpid SET DEFAULT nextval('public.houses_zpid_seq'::regclass);


--
-- Data for Name: User; Type: TABLE DATA; Schema: public; Owner: brand
--

COPY public."User" (id, email, name, image, "favoritePet", "createdAt", "updatedAt", provider, "providerAccountId") FROM stdin;
\.


--
-- Data for Name: _prisma_migrations; Type: TABLE DATA; Schema: public; Owner: brand
--

COPY public._prisma_migrations (id, checksum, finished_at, migration_name, logs, rolled_back_at, started_at, applied_steps_count) FROM stdin;
c6ba3adb-0049-4c53-bd00-b4163bc9db51	59c20921417bc6440141a5999049815ccd496e08306318931327f9259ef40788	2024-12-03 18:22:34.323153-08	20241204022234_init	\N	\N	2024-12-03 18:22:34.287149-08	1
27d834b4-7827-4042-a8e3-29151f77d5cc	bc8e2595874ccef95bf586e3823c322a5b71c8d9eb816e1effe2c5ace9a9d60e	2024-12-07 14:13:52.118872-08	20241207221352_add_provider_fields_to_user	\N	\N	2024-12-07 14:13:52.113222-08	1
\.


--
-- Data for Name: crimes; Type: TABLE DATA; Schema: public; Owner: brand
--

COPY public.crimes (crime_id, type, description, location, date_reported) FROM stdin;
\.


--
-- Data for Name: houses; Type: TABLE DATA; Schema: public; Owner: brand
--

COPY public.houses (zpid, address, price, lat, long) FROM stdin;
7334334	6042 Citation Ct	599000.0	\N	\N
7263244	660 La Rue Ave	739000.0	\N	\N
63239668	908 Edgecliff Dr	630000.0	\N	\N
7297702	5325 Seville Ct	525000.0	\N	\N
7250217	2150 Arcane Ave	619000.0	\N	\N
7330088	14330 E Windriver Ln	789000.0	\N	\N
72652098	2201 Virginia Lake Way	524999.0	\N	\N
70485349	5250 Bellazza Ct	1179000.0	\N	\N
7261128	1855 Mayberry Dr	699900.0	\N	\N
7270817	50 Moore Ln	750000.0	\N	\N
7269795	3323 Susileen Dr	599000.0	\N	\N
7318666	3745 Meadowlark Dr	250000.0	\N	\N
7270401	2199 Humboldt St	749500.0	\N	\N
7305382	12730 Buckthorn Ln	1250000.0	\N	\N
63239886	4000 Goodsell Ln	12900000.0	\N	\N
7248055	3225 Bryan St	550000.0	\N	\N
7335807	2545 Beaumont Pkwy	690000.0	\N	\N
7270522	2315 Homestead Pl	1199000.0	\N	\N
7331725	1644 Rocky Cove Ln	540000.0	\N	\N
7269784	3303 Susileen Dr	794000.0	\N	\N
63239657	4586 Canyon Ridge Ln	595000.0	\N	\N
72669379	7080 Sierra Vista Way	1650000.0	\N	\N
306291884	955 Solarium Dr	1099000.0	\N	\N
7299435	3575 Cashill Blvd	650000.0	\N	\N
7336802	3655 Royer Ct	989000.0	\N	\N
7263271	1035 Lander St	865000.0	\N	\N
7249038	3410 Bowie Rd	369900.0	\N	\N
7254436	2835 Everett Dr	459000.0	\N	\N
7297290	2795 Erminia Rd	1945000.0	\N	\N
7251578	1490 Crown Dr	475000.0	\N	\N
7318941	4040 Goldfinch Dr	210000.0	\N	\N
7319148	3445 Canvasback Ln	399900.0	\N	\N
7254370	2785 Judith Ln	515000.0	\N	\N
7333151	7530 Berryhill Dr	649500.0	\N	\N
7318536	3400 Brant St	390000.0	\N	\N
7255465	2075 W 6th St	485000.0	\N	\N
7333497	6322 Chesterfield Ln	525000.0	\N	\N
7261111	1900 Marla Dr	670000.0	\N	\N
7299498	6955 Windy Hill Way	3750000.0	\N	\N
7297269	40 Lemming Dr	659000.0	\N	\N
7269392	1590 Webster Way	1498888.0	\N	\N
\.


--
-- Data for Name: schools; Type: TABLE DATA; Schema: public; Owner: brand
--

COPY public.schools (name, grades, rating) FROM stdin;
Jessie Beck Elementary School	PK-6	8
Darrell C Swope Middle School	6-8	8
Reno High School	9-12	5
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: brand
--

COPY public.users (account, first_name, last_name, created_on) FROM stdin;
\.


--
-- Name: User_id_seq; Type: SEQUENCE SET; Schema: public; Owner: brand
--

SELECT pg_catalog.setval('public."User_id_seq"', 1, false);


--
-- Name: crimes_crime_id_seq; Type: SEQUENCE SET; Schema: public; Owner: brand
--

SELECT pg_catalog.setval('public.crimes_crime_id_seq', 1, false);


--
-- Name: houses_zpid_seq; Type: SEQUENCE SET; Schema: public; Owner: brand
--

SELECT pg_catalog.setval('public.houses_zpid_seq', 1, false);


--
-- Name: User User_pkey; Type: CONSTRAINT; Schema: public; Owner: brand
--

ALTER TABLE ONLY public."User"
    ADD CONSTRAINT "User_pkey" PRIMARY KEY (id);


--
-- Name: _prisma_migrations _prisma_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: brand
--

ALTER TABLE ONLY public._prisma_migrations
    ADD CONSTRAINT _prisma_migrations_pkey PRIMARY KEY (id);


--
-- Name: crimes crimes_pkey; Type: CONSTRAINT; Schema: public; Owner: brand
--

ALTER TABLE ONLY public.crimes
    ADD CONSTRAINT crimes_pkey PRIMARY KEY (crime_id);


--
-- Name: houses houses_pkey; Type: CONSTRAINT; Schema: public; Owner: brand
--

ALTER TABLE ONLY public.houses
    ADD CONSTRAINT houses_pkey PRIMARY KEY (zpid);


--
-- Name: schools schools_pkey; Type: CONSTRAINT; Schema: public; Owner: brand
--

ALTER TABLE ONLY public.schools
    ADD CONSTRAINT schools_pkey PRIMARY KEY (name);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: brand
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (account);


--
-- Name: User_email_key; Type: INDEX; Schema: public; Owner: brand
--

CREATE UNIQUE INDEX "User_email_key" ON public."User" USING btree (email);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: brand
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;


--
-- PostgreSQL database dump complete
--


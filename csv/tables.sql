--
-- PostgreSQL database dump
--

-- Dumped from database version 11.3
-- Dumped by pg_dump version 11.3

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: players; Type: TABLE; Schema: public; Owner: prsolans
--
DROP TABLE IF EXISTS public.rankings;
DROP TABLE IF EXISTS public.players;
DROP TABLE IF EXISTS public.teams;

CREATE TABLE public.players (
    player_id integer NOT NULL,
    name text,
    age integer,
    experience integer,
    "position" text,
    team_id integer
);

--
-- Name: players_player_id_seq; Type: SEQUENCE; Schema: public; Owner: prsolans
--

CREATE SEQUENCE public.players_player_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

--
-- Name: players_player_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: prsolans
--

ALTER SEQUENCE public.players_player_id_seq OWNED BY public.players.player_id;


--
-- Name: rankings; Type: TABLE; Schema: public; Owner: prsolans
--

CREATE TABLE public.rankings (
    id integer NOT NULL,
    source text,
    value integer,
    text text,
    player_id integer
);

--
-- Name: COLUMN rankings.value; Type: COMMENT; Schema: public; Owner: prsolans
--

COMMENT ON COLUMN public.rankings.value IS 'If there is a numeric metric';

--
-- Name: rankings_id_seq; Type: SEQUENCE; Schema: public; Owner: prsolans
--

CREATE SEQUENCE public.rankings_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: rankings_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: prsolans
--

ALTER SEQUENCE public.rankings_id_seq OWNED BY public.rankings.id;


--
-- Name: teams; Type: TABLE; Schema: public; Owner: prsolans
--

CREATE TABLE public.teams (
    team_id integer NOT NULL,
    city text,
    name text,
    abbreviation text
);


--
-- Name: teams_team_id_seq; Type: SEQUENCE; Schema: public; Owner: prsolans
--

CREATE SEQUENCE public.teams_team_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: teams_team_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: prsolans
--

ALTER SEQUENCE public.teams_team_id_seq OWNED BY public.teams.team_id;


--
-- Name: players player_id; Type: DEFAULT; Schema: public; Owner: prsolans
--

ALTER TABLE ONLY public.players ALTER COLUMN player_id SET DEFAULT nextval('public.players_player_id_seq'::regclass);


--
-- Name: rankings id; Type: DEFAULT; Schema: public; Owner: prsolans
--

ALTER TABLE ONLY public.rankings ALTER COLUMN id SET DEFAULT nextval('public.rankings_id_seq'::regclass);


--
-- Name: teams team_id; Type: DEFAULT; Schema: public; Owner: prsolans
--

ALTER TABLE ONLY public.teams ALTER COLUMN team_id SET DEFAULT nextval('public.teams_team_id_seq'::regclass);


--
-- Name: players players_pkey; Type: CONSTRAINT; Schema: public; Owner: prsolans
--

ALTER TABLE ONLY public.players
    ADD CONSTRAINT players_pkey PRIMARY KEY (player_id);


--
-- Name: rankings rankings_pkey; Type: CONSTRAINT; Schema: public; Owner: prsolans
--

ALTER TABLE ONLY public.rankings
    ADD CONSTRAINT rankings_pkey PRIMARY KEY (id);


--
-- Name: teams teams_pkey; Type: CONSTRAINT; Schema: public; Owner: prsolans
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT teams_pkey PRIMARY KEY (team_id);


--
-- Name: players players_team_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: prsolans
--

ALTER TABLE ONLY public.players
    ADD CONSTRAINT players_team_id_fkey FOREIGN KEY (team_id) REFERENCES public.teams(team_id);


--
-- Name: rankings rankings_player_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: prsolans
--

ALTER TABLE ONLY public.rankings
    ADD CONSTRAINT rankings_player_id_fkey FOREIGN KEY (player_id) REFERENCES public.players(player_id);


--
-- PostgreSQL database dump complete
--


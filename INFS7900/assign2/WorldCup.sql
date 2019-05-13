-- phpMyAdmin SQL Dump
-- version 4.6.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 16, 2018 at 11:39 AM
-- Server version: 5.6.28
-- PHP Version: 5.5.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `WorldCup`
--

-- --------------------------------------------------------

--
-- Table structure for table `COUNTRY`
--

CREATE TABLE `COUNTRY` (
  `Name` char(20) NOT NULL DEFAULT '',
  `Population` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `COUNTRY`
--

INSERT INTO `COUNTRY` (`Name`, `Population`) VALUES
('Australia', 24772247),
('Brazil', 210867954),
('Croatia', 4164783),
('England', 53010000),
('France', 65233271),
('Germany', 82293457),
('Iceland', 337780),
('Italy', 59290969),
('Portugal', 10291196),
('Russia', 143964709),
('South Africa', 57398421),
('South Korea', 51164435),
('Spain', 46397452),
('United Kingdom', 66573504);

-- --------------------------------------------------------

--
-- Table structure for table `CUSTOMER`
--

CREATE TABLE `CUSTOMER` (
  `ID` int(11) NOT NULL DEFAULT '0',
  `Name` char(20) DEFAULT NULL,
  `Email` char(30) DEFAULT NULL,
  `CountryName` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `CUSTOMER`
--

INSERT INTO `CUSTOMER` (`ID`, `Name`, `Email`, `CountryName`) VALUES
(1, 'Lutero Blum', 'lblum0@sina.com.cn', 'United States'),
(2, 'Kerrie Simonassi', 'ksimonassi1@i2i.jp', 'Russia'),
(3, 'Steve Ridhole', 'sridhole2@pen.io', 'Thailand'),
(4, 'Shaun Jakoub', 'sjakoub3@wired.com', 'Iran'),
(5, 'Maris Colborn', 'mcolborn4@narod.ru', 'Russia'),
(6, 'Carr Eilhart', 'ceilhart5@timesonline.co.uk', 'Ukraine'),
(7, 'Nickolas O\'Canavan', 'nocanavan6@aol.com', 'United States'),
(8, 'Jorry Bernath', 'jbernath7@google.it', 'Panama'),
(9, 'Jonas Abendroth', 'jabendroth8@goo.gl', 'Ukraine'),
(10, 'Simeon Kevern', 'skevern9@naver.com', 'Italy'),
(11, 'Leontine Faunch', 'lfauncha@sina.com.cn', 'China'),
(12, 'Sheppard Speake', 'sspeakeb@state.tx.us', 'Indonesia'),
(13, 'Davina Prendergrass', 'dprendergrassc@wikia.com', 'Indonesia'),
(14, 'Brande Bricket', 'bbricketd@omniture.com', 'Brazil'),
(15, 'Roley Fellgett', 'rfellgette@ucoz.ru', 'China'),
(16, 'Brook Challace', 'bchallacef@webs.com', 'Lithuania'),
(17, 'Court Burgyn', 'cburgyng@google.com', 'China'),
(18, 'Renie Heinritz', 'rheinritzh@cyberchimps.com', 'Japan'),
(19, 'Goddard Mansuer', 'gmansueri@bloglovin.com', 'Tuvalu'),
(20, 'Blaire Ruston', 'brustonj@shop-pro.jp', 'Russia'),
(21, 'Sutton Londer', 'slonderk@omniture.com', 'Russia'),
(22, 'Yolanthe Geertsen', 'ygeertsenl@va.gov', 'Croatia'),
(23, 'Jean MacVaugh', 'jmacvaughm@geocities.com', 'Indonesia'),
(24, 'Tamara Gayter', 'tgaytern@bloglovin.com', 'Iran'),
(25, 'Celesta Pyford', 'cpyfordo@nytimes.com', 'Colombia'),
(26, 'Tull Abate', 'tabatep@nyu.edu', 'United States'),
(27, 'Augustus Hassell', 'ahassellq@vinaora.com', 'China'),
(28, 'Vin Malyan', 'vmalyanr@printfriendly.com', 'Morocco'),
(29, 'Boothe Showt', 'bshowts@npr.org', 'Estonia'),
(30, 'Chet Starte', 'cstartet@unesco.org', 'Peru'),
(31, 'Hatty Hebbron', 'hhebbronu@opera.com', 'Sweden'),
(32, 'Catherine Plumstead', 'cplumsteadv@nature.com', 'Russia'),
(33, 'Crystie Drinkale', 'cdrinkalew@nifty.com', 'Malawi'),
(34, 'Claiborne Rushman', 'crushmanx@npr.org', 'Vietnam'),
(35, 'Monte Baulcombe', 'mbaulcombey@ocn.ne.jp', 'Bahamas'),
(36, 'Angela Simion', 'asimionz@cnn.com', 'Canada'),
(37, 'Dave Archdeckne', 'darchdeckne10@reuters.com', 'United States'),
(38, 'Casper Janoschek', 'cjanoschek11@about.me', 'Czech Republic'),
(39, 'Artair Brandolini', 'abrandolini12@senate.gov', 'Mexico'),
(40, 'Callie Foye', 'cfoye13@wufoo.com', 'Philippines'),
(41, 'Virgie Finnimore', 'vfinnimore14@tmall.com', 'Pakistan'),
(42, 'Germain Genner', 'ggenner15@smugmug.com', 'Indonesia'),
(43, 'Liva Cowtherd', 'lcowtherd16@cornell.edu', 'Philippines'),
(44, 'Ainslee Hunstone', 'ahunstone17@artisteer.com', 'Kazakhstan'),
(45, 'Rosalinda Gaffey', 'rgaffey18@cloudflare.com', 'China'),
(46, 'Ninette Stubbeley', 'nstubbeley19@disqus.com', 'Pakistan'),
(47, 'Jeni Manjot', 'jmanjot1a@amazon.co.uk', 'China'),
(48, 'Branden Bangiard', 'bbangiard1b@google.pl', 'Philippines'),
(49, 'John Tunstall', 'jtunstall1c@vistaprint.com', 'Thailand'),
(50, 'Annissa Ratnege', 'aratnege1d@weather.com', 'Egypt'),
(51, 'Merrel Lieber', 'mlieber1e@ning.com', 'Syria'),
(52, 'Barry Itzhaki', 'bitzhaki1f@edublogs.org', 'Brazil'),
(53, 'Fayth Cunney', 'fcunney1g@addthis.com', 'Brazil'),
(54, 'Valentina Glencrosch', 'vglencrosche1h@oracle.com', 'Sweden'),
(55, 'Cori Graveson', 'cgraveson1i@flickr.com', 'Greece'),
(56, 'Meggie Dimont', 'mdimont1j@abc.net.au', 'Indonesia'),
(57, 'Noelle Sebert', 'nsebert1k@biblegateway.com', 'Ukraine'),
(58, 'Lyell Reburn', 'lreburn1l@bbb.org', 'Indonesia'),
(59, 'Jacinthe Hurnell', 'jhurnell1m@opera.com', 'Ukraine'),
(60, 'Martin Roswarne', 'mroswarne1n@vinaora.com', 'France'),
(61, 'Nicola Lorain', 'nlorain1o@tinypic.com', 'China'),
(62, 'Siegfried McDunlevy', 'smcdunlevy1p@paginegialle.it', 'Brazil'),
(63, 'Aron Cainey', 'acainey1q@huffingtonpost.com', 'China'),
(64, 'Isac Storre', 'istorre1r@miitbeian.gov.cn', 'China'),
(65, 'Patrick Yashunin', 'pyashunin1s@cdbaby.com', 'Indonesia'),
(66, 'Tammy Alderwick', 'talderwick1t@comcast.net', 'China'),
(67, 'Kingsly Worden', 'kworden1u@ustream.tv', 'Iran'),
(68, 'Hamil Jochen', 'hjochen1v@weibo.com', 'Dominican Republic'),
(69, 'Kirbee MacCafferty', 'kmaccafferty1w@washingtonpost.', 'China'),
(70, 'Christiano Eccersley', 'ceccersley1x@apache.org', 'Latvia'),
(71, 'Matilde Wriggleswort', 'mwrigglesworth1y@toplist.cz', 'Paraguay'),
(72, 'Elisha Syrad', 'esyrad1z@bigcartel.com', 'Sweden'),
(73, 'George Kruse', 'gkruse20@wix.com', 'Iran'),
(74, 'Berni Allan', 'ballan21@latimes.com', 'Sweden'),
(75, 'Lane Thaw', 'lthaw22@nasa.gov', 'Philippines'),
(76, 'Benedetto Ambrozewic', 'bambrozewicz23@tmall.com', 'Norway'),
(77, 'Pamella Folks', 'pfolks24@macromedia.com', 'China'),
(78, 'Cecile Selesnick', 'cselesnick25@virginia.edu', 'Uruguay'),
(79, 'Verney Mocher', 'vmocher26@dyndns.org', 'South Africa'),
(80, 'Marti Elix', 'melix27@elpais.com', 'China'),
(81, 'Elwood Trower', 'etrower28@yahoo.com', 'China'),
(82, 'Addy Blindermann', 'ablindermann29@arstechnica.com', 'China'),
(83, 'Lucien Bradwell', 'lbradwell2a@sphinn.com', 'Thailand'),
(84, 'Armando Pavelin', 'apavelin2b@va.gov', 'Mexico'),
(85, 'Libby Schaumaker', 'lschaumaker2c@reverbnation.com', 'Russia'),
(86, 'Paige Anthoine', 'panthoine2d@blogtalkradio.com', 'Ireland'),
(87, 'Artie Koch', 'akoch2e@admin.ch', 'Mexico'),
(88, 'Arvin Byk', 'abyk2f@weibo.com', 'Russia'),
(89, 'Tabatha Boxhill', 'tboxhill2g@facebook.com', 'Brazil'),
(90, 'Cassandra Lytle', 'clytle2h@elpais.com', 'Madagascar'),
(91, 'Gwendolyn Manass', 'gmanass2i@indiegogo.com', 'China'),
(92, 'Clemmie Sargood', 'csargood2j@vinaora.com', 'China'),
(93, 'Kip Cullimore', 'kcullimore2k@reverbnation.com', 'Mexico'),
(94, 'Glad Prigg', 'gprigg2l@privacy.gov.au', 'Paraguay'),
(95, 'Farris Kettlestringe', 'fkettlestringe2m@pbs.org', 'China'),
(96, 'Saunder MacWhan', 'smacwhan2n@mozilla.org', 'Hungary'),
(97, 'Yolanda Tremathick', 'ytremathick2o@t-online.de', 'Philippines'),
(98, 'Everard Sawdy', 'esawdy2p@theatlantic.com', 'Philippines'),
(99, 'Vivi McWard', 'vmcward2q@home.pl', 'China'),
(100, 'Spence MacAscaidh', 'smacascaidh2r@ning.com', 'Brazil');

-- --------------------------------------------------------

--
-- Table structure for table `ELIMINATIONGAME`
--

CREATE TABLE `ELIMINATIONGAME` (
  `ID` int(11) NOT NULL DEFAULT '0',
  `Stage` char(30) DEFAULT NULL,
  `HomePenalties` int(11) DEFAULT NULL,
  `AwayPenalties` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `ELIMINATIONGAME`
--

INSERT INTO `ELIMINATIONGAME` (`ID`, `Stage`, `HomePenalties`, `AwayPenalties`) VALUES
(26, 'quarter-final', 0, 1),
(27, 'quarter-final', 2, 1),
(28, 'quarter-final', 1, 0),
(29, 'quarter-final', 0, 2),
(30, 'semi-fianl', 0, 0),
(31, 'semi-fianl', 1, 0),
(32, 'play-off for third place', 0, 1),
(33, 'final', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `GOALS`
--

CREATE TABLE `GOALS` (
  `PlayerID` int(11) NOT NULL DEFAULT '0',
  `MatchID` int(11) NOT NULL DEFAULT '0',
  `Count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `GOALS`
--

INSERT INTO `GOALS` (`PlayerID`, `MatchID`, `Count`) VALUES
(3, 4, 1),
(3, 5, 1),
(3, 28, 2),
(6, 28, 1),
(7, 3, 2),
(12, 1, 2),
(12, 26, 1),
(14, 3, 2),
(15, 8, 1),
(15, 30, 3),
(15, 33, 1),
(20, 11, 1),
(22, 30, 1),
(29, 12, 2),
(29, 22, 1),
(30, 33, 1),
(37, 13, 3),
(40, 11, 2),
(48, 24, 2),
(48, 25, 1),
(51, 10, 2),
(57, 14, 1),
(57, 18, 1),
(57, 20, 1),
(57, 24, 1),
(57, 25, 1),
(58, 30, 1);

-- --------------------------------------------------------

--
-- Table structure for table `HOMECLUB`
--

CREATE TABLE `HOMECLUB` (
  `Name` char(20) NOT NULL DEFAULT '',
  `Country` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `HOMECLUB`
--

INSERT INTO `HOMECLUB` (`Name`, `Country`) VALUES
('English', 'England'),
('A.C. Milan', 'Italy'),
('Inter Milan', 'Italy'),
('Juventus', 'Italy'),
('FC Barcelona', 'Spain'),
('Real Madrid', 'Spain'),
('Liverpool', 'United Kingdom'),
('Manchester United', 'United Kingdom');

-- --------------------------------------------------------

--
-- Table structure for table `MATCH`
--

CREATE TABLE `MATCH` (
  `ID` int(11) NOT NULL DEFAULT '0',
  `Date` date DEFAULT NULL,
  `Time` time DEFAULT NULL,
  `Stadium` char(20) DEFAULT NULL,
  `HomeYear` int(11) DEFAULT NULL,
  `HomeTeamID` int(11) DEFAULT NULL,
  `AwayYear` int(11) DEFAULT NULL,
  `AwayTeamID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `MATCH`
--

INSERT INTO `MATCH` (`ID`, `Date`, `Time`, `Stadium`, `HomeYear`, `HomeTeamID`, `AwayYear`, `AwayTeamID`) VALUES
(1, '2018-06-14', '13:00:00', 'Luzhniki', 2018, 1, 2018, 2),
(2, '2018-06-14', '17:00:00', 'Luzhniki', 2018, 1, 2018, 5),
(3, '2018-06-14', '13:00:00', 'Ekaterinburg', 2018, 3, 2018, 4),
(4, '2018-06-15', '13:00:00', 'Ekaterinburg', 2018, 3, 2018, 5),
(5, '2018-06-15', '21:00:00', 'Ekaterinburg', 2018, 3, 2018, 2),
(6, '2018-06-15', '13:00:00', 'Saint Petersburg', 2018, 4, 2018, 1),
(7, '2018-06-16', '13:00:00', 'Saint Petersburg', 2018, 4, 2018, 2),
(8, '2018-06-16', '21:00:00', 'Saint Petersburg', 2018, 4, 2018, 5),
(9, '2018-06-16', '21:00:00', 'Luzhniki', 2018, 1, 2018, 3),
(10, '2018-06-17', '13:00:00', 'Kazan', 2018, 2, 2018, 5),
(11, '2018-06-14', '13:00:00', 'Saint Petersburg', 2018, 6, 2018, 7),
(12, '2018-06-14', '21:00:00', 'Saint Petersburg', 2018, 6, 2018, 8),
(13, '2018-06-14', '13:00:00', 'Nizhny Novgorod', 2018, 9, 2018, 10),
(14, '2018-06-14', '21:00:00', 'Nizhny Novgorod', 2018, 9, 2018, 11),
(15, '2018-06-15', '21:00:00', 'Saint Petersburg', 2018, 6, 2018, 9),
(16, '2018-06-15', '13:00:00', 'Fisht', 2018, 7, 2018, 8),
(17, '2018-06-15', '21:00:00', 'Fisht', 2018, 7, 2018, 10),
(18, '2018-06-15', '13:00:00', 'Kazan', 2018, 11, 2018, 6),
(19, '2018-06-16', '13:00:00', 'Kazan', 2018, 10, 2018, 6),
(20, '2018-06-16', '21:00:00', 'Kazan', 2018, 10, 2018, 11),
(21, '2018-06-16', '13:00:00', 'Fisht', 2018, 7, 2018, 9),
(22, '2018-06-16', '21:00:00', 'Nizhny Novgorod', 2018, 9, 2018, 8),
(23, '2018-06-17', '13:00:00', 'Fisht', 2018, 8, 2018, 10),
(24, '2018-06-17', '21:00:00', 'Fisht', 2018, 8, 2018, 11),
(25, '2018-06-18', '17:00:00', 'Kazan', 2018, 11, 2018, 7),
(26, '2018-06-28', '13:00:00', 'Luzhniki', 2018, 1, 2018, 2),
(27, '2018-06-28', '13:00:00', 'Fisht', 2018, 8, 2018, 5),
(28, '2018-06-28', '13:00:00', 'Ekaterinburg', 2018, 3, 2018, 4),
(29, '2018-06-28', '13:00:00', 'Nizhny Novgorod', 2018, 9, 2018, 7),
(30, '2018-06-30', '17:00:00', 'Saint Petersburg', 2018, 4, 2018, 1),
(31, '2018-06-30', '17:00:00', 'Fisht', 2018, 8, 2018, 9),
(32, '2018-07-06', '21:00:00', 'Luzhniki', 2018, 1, 2018, 9),
(33, '2018-07-15', '18:00:00', 'Saint Petersburg', 2018, 4, 2018, 8);

-- --------------------------------------------------------

--
-- Table structure for table `MEMBER`
--

CREATE TABLE `MEMBER` (
  `ID` int(11) NOT NULL DEFAULT '0',
  `Name` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `MEMBER`
--

INSERT INTO `MEMBER` (`ID`, `Name`) VALUES
(1, 'Markos Bricknall'),
(2, 'Joshua Shillan'),
(3, 'Alvina Meiklejohn'),
(4, 'Kari Callard'),
(5, 'Merrick Rowlstone'),
(6, 'Elke Berryman'),
(7, 'Verne Blowing'),
(8, 'Vonnie Cayley'),
(9, 'Dimitri Grimwade'),
(10, 'Roderigo Arendt'),
(11, 'Henriette Tesyro'),
(12, 'Jonathon Hellis'),
(13, 'Louie Le Marquand'),
(14, 'Winonah Jon'),
(15, 'Ring Thatcham'),
(16, 'Joyous Hornung'),
(17, 'Emlyn Aisthorpe'),
(18, 'Leonidas Fawley'),
(19, 'Warner Chestney'),
(20, 'Cece Heath'),
(21, 'Krystle Desbrow'),
(22, 'Elisabetta Pendlebur'),
(23, 'Anatol Truelock'),
(24, 'Sheffield Sprosson'),
(25, 'Imelda Britton'),
(26, 'Paulie Quick'),
(27, 'Gasparo Grinikhin'),
(28, 'Alvinia Edwardson'),
(29, 'Cameron Lenahan'),
(30, 'Evangeline Vallerine'),
(31, 'Annabel Readshaw'),
(32, 'Gray Raden'),
(33, 'Demetrius Rosettini'),
(34, 'Ettore McCreary'),
(35, 'Bethena Wooderson'),
(36, 'Allie Bunson'),
(37, 'Vincents Denne'),
(38, 'Tiphany Leech'),
(39, 'Randi O\'Hoolahan'),
(40, 'Shea O\'Nowlan'),
(41, 'Oralie Streeten'),
(42, 'Cherish Hunnybun'),
(43, 'Sidoney Pashen'),
(44, 'Wendall Rosa'),
(45, 'Bernhard Challin'),
(46, 'Odette Wooffitt'),
(47, 'Perri Tallet'),
(48, 'Bartholomew Arnaudi'),
(49, 'Donelle McDuffy'),
(50, 'Vannie McShane'),
(51, 'Johanna Diggle'),
(52, 'Stacee Lumsdale'),
(53, 'Rossie Blissett'),
(54, 'Abbi Leys'),
(55, 'Claybourne Valerio'),
(56, 'Ailina Lethbrig'),
(57, 'Guinevere Creighton'),
(58, 'Tatum O\'Loughane'),
(59, 'Katerine Peacop'),
(60, 'Paten Guerreiro'),
(61, 'Nettie Fursland'),
(62, 'Irvin McTavish'),
(63, 'Marjory Matteoni'),
(64, 'Janie Heephy'),
(65, 'Jimmie Laker'),
(66, 'Fielding Nolleau'),
(67, 'Goldarina Alcido'),
(68, 'Mateo Rothchild'),
(69, 'Brandie Alejo'),
(70, 'Gertrude Gentreau'),
(71, 'Ninetta Autry'),
(72, 'Hildy Andersen'),
(73, 'Sela Longfield'),
(74, 'Elladine Menego'),
(75, 'Arleyne Poltun'),
(76, 'Salmon Collibear'),
(77, 'Claudine Cowderay'),
(78, 'Camellia Boncore'),
(79, 'Charmine Nineham'),
(80, 'Sharon Noirel'),
(81, 'Kylen Sturdgess'),
(82, 'Nomi Shingles'),
(83, 'Gaspard Smy'),
(84, 'Ibbie Jack'),
(85, 'Ferdie Keedwell'),
(86, 'Anett Bayley'),
(87, 'Courtenay Dunthorn'),
(88, 'Khalil Brown'),
(89, 'Maryjane Crittal'),
(90, 'Quint Gwilt'),
(91, 'Kelley Gypps'),
(92, 'Ophelie Wilhelmy'),
(93, 'Gilda Waghorne'),
(94, 'Waneta Davenhill'),
(95, 'Ximenez Yu'),
(96, 'Cindy Spadari'),
(97, 'Meredith Popelay'),
(98, 'Cicily Mansuer'),
(99, 'Allis Redfield'),
(100, 'Andrea Wetherhead');

-- --------------------------------------------------------

--
-- Table structure for table `PLAYER`
--

CREATE TABLE `PLAYER` (
  `ID` int(11) NOT NULL DEFAULT '0',
  `Positin` char(20) DEFAULT NULL,
  `HomeClubName` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `PLAYER`
--

INSERT INTO `PLAYER` (`ID`, `Positin`, `HomeClubName`) VALUES
(3, 'Defender', 'A.C. Milan'),
(6, 'Forward', 'A.C. Milan'),
(7, 'Forward', 'A.C. Milan'),
(8, 'Forward', 'A.C. Milan'),
(12, 'Midfielder', 'Inter Milan'),
(14, 'Forward', 'Inter Milan'),
(15, 'Forward', 'Inter Milan'),
(17, 'Goalkeeper', 'Juventus'),
(19, 'Defender', 'Juventus'),
(20, 'Midfielder', 'Juventus'),
(22, 'Forward', 'Juventus'),
(29, 'Midfielder', 'FC Barcelona'),
(30, 'Forward', 'FC Barcelona'),
(33, 'Goalkeeper', 'Real Madrid'),
(37, 'Midfielder', 'English'),
(38, 'Forward', 'Real Madrid'),
(39, 'Forward', 'Real Madrid'),
(40, 'Goalkeeper', 'English'),
(48, 'Midfielder', 'Liverpool'),
(50, 'Forward', 'Liverpool'),
(51, 'Forward', 'Liverpool'),
(57, 'Forward', 'Manchester United'),
(58, 'Forward', 'Manchester United');

-- --------------------------------------------------------

--
-- Table structure for table `POOLGAME`
--

CREATE TABLE `POOLGAME` (
  `ID` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `POOLGAME`
--

INSERT INTO `POOLGAME` (`ID`) VALUES
(2),
(4),
(6),
(10),
(15),
(16),
(20),
(25);

-- --------------------------------------------------------

--
-- Table structure for table `SAVES`
--

CREATE TABLE `SAVES` (
  `PlayerID` int(11) NOT NULL DEFAULT '0',
  `MatchID` int(11) NOT NULL DEFAULT '0',
  `Count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `SAVES`
--

INSERT INTO `SAVES` (`PlayerID`, `MatchID`, `Count`) VALUES
(3, 4, 1),
(3, 28, 1),
(6, 5, 2),
(6, 9, 2),
(7, 5, 3),
(7, 9, 1),
(7, 28, 2),
(12, 1, 1),
(12, 32, 1),
(15, 3, 1),
(19, 11, 2),
(19, 19, 1),
(29, 12, 1),
(29, 23, 1),
(29, 27, 2),
(29, 33, 3),
(30, 12, 1),
(30, 27, 2),
(30, 33, 1),
(38, 14, 2),
(38, 21, 3),
(40, 11, 3),
(40, 19, 2),
(50, 13, 3),
(51, 1, 2),
(57, 25, 2),
(58, 30, 1),
(58, 32, 3);

-- --------------------------------------------------------

--
-- Table structure for table `SUPPORTSTAFF`
--

CREATE TABLE `SUPPORTSTAFF` (
  `ID` int(11) NOT NULL DEFAULT '0',
  `Role` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `SUPPORTSTAFF`
--

INSERT INTO `SUPPORTSTAFF` (`ID`, `Role`) VALUES
(59, 'President'),
(60, 'President'),
(61, 'President'),
(62, 'President'),
(63, 'President'),
(64, 'President'),
(65, 'President'),
(66, 'President'),
(67, 'President'),
(68, 'President'),
(69, 'President'),
(70, 'Secretary'),
(71, 'Secretary'),
(72, 'Secretary'),
(73, 'Tresureer'),
(74, 'Tresureer'),
(75, 'Manager'),
(76, 'Manager'),
(77, 'Manager'),
(78, 'Manager'),
(79, 'Manager'),
(80, 'Manager'),
(81, 'Manager'),
(82, 'Manager'),
(83, 'Manager'),
(84, 'Manager'),
(85, 'Manager'),
(86, 'Manager'),
(87, 'Manager'),
(88, 'Manager'),
(89, 'Manager'),
(90, 'Medical trainer'),
(91, 'Medical trainer'),
(92, 'Medical trainer'),
(93, 'Medical trainer'),
(94, 'Medical trainer'),
(95, 'Medical trainer'),
(96, 'Medical trainer'),
(97, 'Medical trainer'),
(98, 'Medical trainer'),
(99, 'Medical trainer'),
(100, 'Medical trainer');

-- --------------------------------------------------------

--
-- Table structure for table `TEAM`
--

CREATE TABLE `TEAM` (
  `Year` int(11) NOT NULL DEFAULT '0',
  `ID` int(11) NOT NULL DEFAULT '0',
  `Country` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `TEAM`
--

INSERT INTO `TEAM` (`Year`, `ID`, `Country`) VALUES
(2014, 10, 'Australia'),
(2018, 10, 'Australia'),
(2010, 8, 'Brazil'),
(2014, 8, 'Brazil'),
(2018, 8, 'Brazil'),
(2010, 6, 'Croatia'),
(2014, 6, 'Croatia'),
(2018, 6, 'Croatia'),
(2002, 3, 'France'),
(2006, 3, 'France'),
(2010, 3, 'France'),
(2014, 3, 'France'),
(2018, 3, 'France'),
(2002, 5, 'Germany'),
(2006, 5, 'Germany'),
(2010, 5, 'Germany'),
(2014, 5, 'Germany'),
(2018, 5, 'Germany'),
(2018, 11, 'Iceland'),
(2002, 2, 'Italy'),
(2006, 2, 'Italy'),
(2010, 2, 'Italy'),
(2014, 2, 'Italy'),
(2018, 2, 'Italy'),
(2010, 9, 'Portugal'),
(2014, 9, 'Portugal'),
(2018, 9, 'Portugal'),
(2010, 7, 'Russia'),
(2014, 7, 'Russia'),
(2018, 7, 'Russia'),
(2002, 1, 'Spain'),
(2006, 1, 'Spain'),
(2010, 1, 'Spain'),
(2014, 1, 'Spain'),
(2018, 1, 'Spain'),
(2002, 4, 'United Kingdom'),
(2006, 4, 'United Kingdom'),
(2010, 4, 'United Kingdom'),
(2014, 4, 'United Kingdom'),
(2018, 4, 'United Kingdom');

-- --------------------------------------------------------

--
-- Table structure for table `TEAMMEMBER`
--

CREATE TABLE `TEAMMEMBER` (
  `Year` int(11) NOT NULL DEFAULT '0',
  `TeamID` int(11) NOT NULL DEFAULT '0',
  `MemberID` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `TEAMMEMBER`
--

INSERT INTO `TEAMMEMBER` (`Year`, `TeamID`, `MemberID`) VALUES
(2002, 1, 1),
(2006, 1, 1),
(2010, 1, 1),
(2014, 1, 1),
(2018, 1, 1),
(2002, 1, 2),
(2006, 1, 2),
(2010, 1, 2),
(2018, 1, 2),
(2002, 3, 3),
(2006, 3, 3),
(2010, 3, 3),
(2014, 3, 3),
(2018, 3, 3),
(2002, 3, 4),
(2006, 3, 4),
(2010, 3, 4),
(2014, 3, 4),
(2018, 3, 4),
(2010, 7, 5),
(2014, 7, 5),
(2018, 7, 5),
(2002, 3, 6),
(2006, 3, 6),
(2010, 3, 6),
(2014, 3, 6),
(2018, 3, 6),
(2010, 3, 7),
(2014, 3, 7),
(2018, 3, 7),
(2010, 3, 8),
(2014, 3, 8),
(2018, 3, 8),
(2002, 3, 9),
(2006, 3, 9),
(2010, 3, 9),
(2014, 3, 9),
(2018, 3, 9),
(2010, 7, 10),
(2014, 7, 10),
(2018, 7, 10),
(2010, 7, 11),
(2014, 7, 11),
(2018, 7, 11),
(2002, 1, 12),
(2006, 1, 12),
(2010, 1, 12),
(2014, 1, 12),
(2018, 1, 12),
(2002, 4, 13),
(2006, 4, 13),
(2010, 4, 13),
(2014, 4, 13),
(2018, 4, 13),
(2002, 4, 14),
(2006, 4, 14),
(2010, 4, 14),
(2014, 4, 14),
(2018, 4, 14),
(2002, 4, 15),
(2006, 4, 15),
(2010, 4, 15),
(2014, 4, 15),
(2018, 4, 15),
(2002, 4, 16),
(2006, 4, 16),
(2010, 4, 16),
(2014, 4, 16),
(2018, 4, 16),
(2002, 4, 17),
(2006, 4, 17),
(2010, 4, 17),
(2014, 4, 17),
(2018, 4, 17),
(2002, 4, 18),
(2006, 4, 18),
(2010, 4, 18),
(2014, 4, 18),
(2018, 4, 18),
(2010, 6, 19),
(2014, 6, 19),
(2018, 6, 19),
(2010, 6, 20),
(2014, 6, 20),
(2018, 6, 20),
(2010, 7, 21),
(2014, 7, 21),
(2018, 7, 21),
(2002, 1, 22),
(2006, 1, 22),
(2010, 1, 22),
(2014, 1, 22),
(2018, 1, 22),
(2002, 5, 23),
(2006, 5, 23),
(2010, 5, 23),
(2014, 5, 23),
(2018, 5, 23),
(2002, 5, 24),
(2006, 5, 24),
(2010, 5, 24),
(2014, 5, 24),
(2018, 5, 24),
(2002, 5, 25),
(2006, 5, 25),
(2010, 5, 25),
(2014, 5, 25),
(2018, 5, 25),
(2002, 5, 26),
(2006, 5, 26),
(2010, 5, 26),
(2014, 5, 26),
(2018, 5, 26),
(2002, 5, 27),
(2006, 5, 27),
(2010, 5, 27),
(2014, 5, 27),
(2018, 5, 27),
(2002, 5, 28),
(2006, 5, 28),
(2010, 5, 28),
(2014, 5, 28),
(2018, 5, 28),
(2010, 8, 29),
(2014, 8, 29),
(2018, 8, 29),
(2010, 8, 30),
(2014, 8, 30),
(2018, 8, 30),
(2014, 8, 31),
(2018, 8, 31),
(2002, 2, 32),
(2006, 2, 32),
(2010, 2, 32),
(2014, 2, 32),
(2018, 2, 32),
(2010, 8, 33),
(2014, 8, 33),
(2018, 8, 33),
(2010, 8, 34),
(2014, 8, 34),
(2018, 8, 34),
(2010, 9, 35),
(2014, 9, 35),
(2018, 9, 35),
(2010, 9, 36),
(2014, 9, 36),
(2018, 9, 36),
(2014, 10, 37),
(2018, 10, 37),
(2010, 9, 38),
(2014, 9, 38),
(2018, 9, 38),
(2010, 6, 39),
(2014, 6, 39),
(2018, 6, 39),
(2010, 6, 40),
(2014, 6, 40),
(2018, 6, 40),
(2002, 2, 41),
(2006, 2, 41),
(2010, 2, 41),
(2014, 2, 41),
(2018, 2, 41),
(2018, 9, 44),
(2014, 10, 45),
(2018, 10, 45),
(2014, 10, 46),
(2018, 10, 46),
(2018, 11, 47),
(2018, 11, 48),
(2002, 2, 49),
(2006, 2, 49),
(2010, 2, 49),
(2014, 2, 49),
(2018, 2, 49),
(2014, 10, 50),
(2018, 10, 50),
(2002, 2, 51),
(2006, 2, 51),
(2010, 2, 51),
(2014, 2, 51),
(2018, 2, 51),
(2002, 2, 52),
(2006, 2, 52),
(2010, 2, 52),
(2014, 2, 52),
(2018, 2, 52),
(2018, 11, 54),
(2018, 11, 55),
(2018, 11, 57),
(2010, 1, 58),
(2014, 1, 58),
(2018, 1, 58),
(2006, 1, 59),
(2010, 1, 59),
(2014, 1, 59),
(2018, 1, 59),
(2014, 3, 60),
(2018, 3, 60),
(2014, 5, 61),
(2018, 5, 61),
(2010, 6, 62),
(2014, 6, 62),
(2018, 6, 62),
(2010, 7, 63),
(2014, 7, 63),
(2018, 7, 63),
(2018, 8, 63),
(2010, 9, 64),
(2014, 9, 64),
(2018, 9, 64),
(2018, 10, 65),
(2018, 11, 66),
(2002, 4, 68),
(2006, 4, 68),
(2010, 4, 68),
(2014, 4, 68),
(2018, 4, 68),
(2018, 2, 69),
(2018, 1, 70),
(2018, 3, 71),
(2018, 3, 73),
(2018, 11, 74),
(2002, 1, 75),
(2006, 1, 75),
(2010, 1, 75),
(2014, 1, 75),
(2018, 1, 75),
(2014, 1, 76),
(2018, 1, 76),
(2002, 2, 77),
(2006, 2, 77),
(2010, 2, 77),
(2014, 2, 77),
(2018, 2, 77),
(2014, 2, 78),
(2018, 2, 78),
(2006, 4, 79),
(2010, 4, 79),
(2014, 4, 79),
(2018, 4, 79),
(2014, 9, 80),
(2018, 9, 80),
(2014, 9, 81),
(2018, 9, 81),
(2014, 10, 82),
(2018, 10, 82),
(2018, 11, 87),
(2018, 7, 88),
(2002, 3, 89),
(2006, 3, 89),
(2010, 3, 89),
(2014, 3, 89),
(2018, 3, 89),
(2002, 1, 90),
(2006, 1, 90),
(2010, 1, 90),
(2014, 1, 90),
(2018, 1, 90),
(2014, 2, 91),
(2018, 2, 91),
(2006, 3, 92),
(2010, 3, 92),
(2014, 3, 92),
(2018, 3, 92),
(2010, 4, 93),
(2014, 4, 93),
(2018, 4, 93),
(2002, 5, 94),
(2006, 5, 94),
(2010, 5, 94),
(2014, 5, 94),
(2018, 5, 94),
(2018, 7, 94),
(2010, 8, 95),
(2014, 8, 95),
(2018, 8, 95),
(2014, 10, 96),
(2018, 10, 96),
(2018, 11, 97),
(2018, 11, 98);

-- --------------------------------------------------------

--
-- Table structure for table `TICKET`
--

CREATE TABLE `TICKET` (
  `MatchID` int(11) NOT NULL DEFAULT '0',
  `Ticket#` int(11) NOT NULL DEFAULT '0',
  `CustomerID` int(11) DEFAULT NULL,
  `Price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `TICKET`
--

INSERT INTO `TICKET` (`MatchID`, `Ticket#`, `CustomerID`, `Price`) VALUES
(2, 6103, 4, 105),
(2, 6104, 5, 105),
(3, 6105, 6, 205),
(3, 6106, 44, 105),
(3, 6107, 8, 205),
(4, 6108, 9, 105),
(4, 6109, 34, 105),
(4, 6110, 11, 105),
(5, 6111, 12, 205),
(5, 6112, 78, 105),
(6, 6113, 14, 105),
(6, 6114, 15, 305),
(6, 6115, 23, 105),
(7, 6116, 17, 205),
(7, 6117, 18, 105),
(7, 6118, 6, 205),
(8, 6119, 20, 105),
(8, 6120, 21, 105),
(8, 6121, 22, 305),
(9, 6122, 23, 105),
(9, 6123, 24, 105),
(10, 6124, 5, 105),
(10, 6125, 26, 105),
(11, 6126, 27, 305),
(11, 6127, 28, 105),
(11, 6128, 29, 105),
(12, 6129, 3, 105),
(12, 6130, 31, 205),
(12, 6131, 32, 105),
(12, 6132, 33, 105),
(13, 6133, 34, 105),
(13, 6134, 35, 105),
(14, 6135, 11, 205),
(14, 6136, 37, 105),
(15, 6137, 38, 105),
(15, 6138, 39, 105),
(15, 6139, 40, 105),
(16, 6140, 41, 205),
(16, 6141, 42, 105),
(17, 6142, 22, 105),
(17, 6143, 44, 105),
(17, 6144, 45, 105),
(18, 6145, 46, 405),
(18, 6146, 47, 105),
(18, 6147, 48, 105),
(18, 6148, 2, 105),
(19, 6149, 50, 105),
(19, 6150, 51, 405),
(19, 6151, 6, 105),
(19, 6152, 53, 105),
(19, 6153, 9, 105),
(20, 6154, 55, 105),
(20, 6155, 56, 105),
(21, 6156, 57, 105),
(21, 6157, 58, 305),
(21, 6158, 12, 105),
(22, 6159, 60, 105),
(22, 6160, 61, 105),
(22, 6161, 14, 105),
(22, 6162, 63, 305),
(22, 6163, 64, 105),
(22, 6164, 65, 105),
(23, 6165, 15, 105),
(23, 6166, 67, 205),
(24, 6167, 68, 105),
(24, 6168, 69, 105),
(24, 6169, 16, 305),
(25, 6170, 71, 105),
(25, 6171, 72, 105),
(25, 6172, 73, 105),
(26, 6600, 18, 455),
(26, 6601, 75, 655),
(26, 6602, 76, 455),
(26, 6603, 77, 455),
(26, 6604, 78, 455),
(26, 6605, 12, 455),
(26, 6606, 80, 455),
(26, 6607, 81, 455),
(26, 6608, 82, 755),
(26, 6609, 83, 455),
(26, 6610, 25, 455),
(26, 6611, 85, 455),
(26, 6612, 86, 555),
(26, 6613, 87, 455),
(27, 6614, 88, 455),
(27, 6615, 27, 455),
(27, 6616, 90, 455),
(27, 6617, 91, 655),
(27, 6618, 92, 455),
(27, 6619, 24, 455),
(27, 6620, 94, 455),
(27, 6621, 95, 455),
(27, 6622, 96, 755),
(27, 6623, 97, 455),
(27, 6624, 23, 455),
(27, 6625, 99, 455),
(28, 6626, 1, 455),
(28, 6627, 45, 555),
(28, 6628, 2, 455),
(28, 6629, 3, 455),
(28, 6630, 67, 455),
(28, 6631, 5, 655),
(28, 6632, 6, 455),
(28, 6633, 7, 455),
(28, 6634, 8, 655),
(29, 6635, 9, 455),
(29, 6636, 34, 455),
(29, 6637, 11, 455),
(29, 6638, 12, 555),
(29, 6639, 13, 455),
(29, 6640, 14, 455),
(29, 6641, 78, 455),
(29, 6642, 16, 555),
(29, 6643, 17, 455),
(29, 6644, 97, 455),
(30, 6645, 19, 550),
(30, 6646, 20, 550),
(30, 6647, 21, 550),
(30, 6648, 22, 650),
(30, 6649, 34, 750),
(30, 6650, 24, 550),
(30, 6651, 25, 650),
(30, 6652, 26, 550),
(31, 6653, 27, 550),
(31, 6654, 76, 550),
(31, 6655, 29, 650),
(31, 6656, 30, 550),
(31, 6657, 31, 750),
(31, 6658, 32, 550),
(31, 6659, 4, 550),
(31, 6660, 34, 550),
(31, 6661, 35, 750),
(31, 6662, 36, 750),
(31, 6663, 37, 550),
(31, 6664, 38, 550),
(32, 6665, 2, 550),
(32, 6666, 40, 650),
(32, 6667, 41, 650),
(32, 6668, 42, 550),
(32, 6669, 6, 550),
(32, 6670, 44, 550),
(33, 6671, 12, 1100),
(33, 6672, 46, 1100),
(33, 6673, 47, 1100),
(33, 6674, 48, 1200),
(33, 6675, 14, 1300),
(33, 6676, 50, 1100),
(33, 6677, 51, 1100),
(33, 6678, 52, 1200),
(33, 6679, 16, 1200),
(33, 6680, 54, 1100),
(33, 6681, 55, 1100),
(33, 6682, 56, 1100),
(33, 6683, 1, 1100),
(33, 6684, 5, 1100),
(33, 6685, 59, 1300),
(33, 6686, 60, 1100),
(33, 6687, 61, 1200),
(33, 6688, 62, 1100),
(33, 6689, 3, 1100),
(33, 6690, 1, 1100),
(33, 6691, 65, 1200),
(33, 6692, 66, 1100),
(33, 6693, 67, 1300),
(33, 6694, 13, 1100),
(33, 6695, 69, 1100);

-- --------------------------------------------------------

--
-- Table structure for table `TOURNAMENT`
--

CREATE TABLE `TOURNAMENT` (
  `Year` int(11) NOT NULL DEFAULT '0',
  `Country` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `TOURNAMENT`
--

INSERT INTO `TOURNAMENT` (`Year`, `Country`) VALUES
(2014, 'Brazil'),
(2006, 'Germany'),
(2018, 'Russia'),
(2010, 'South Africa'),
(2002, 'South Korea');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `COUNTRY`
--
ALTER TABLE `COUNTRY`
  ADD PRIMARY KEY (`Name`);

--
-- Indexes for table `CUSTOMER`
--
ALTER TABLE `CUSTOMER`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `ELIMINATIONGAME`
--
ALTER TABLE `ELIMINATIONGAME`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `GOALS`
--
ALTER TABLE `GOALS`
  ADD PRIMARY KEY (`PlayerID`,`MatchID`),
  ADD KEY `FK_GOALS_MatchID` (`MatchID`);

--
-- Indexes for table `HOMECLUB`
--
ALTER TABLE `HOMECLUB`
  ADD PRIMARY KEY (`Name`),
  ADD KEY `FK_HOMECLUB_Country` (`Country`);

--
-- Indexes for table `MATCH`
--
ALTER TABLE `MATCH`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `HomeYear` (`HomeYear`,`HomeTeamID`,`AwayYear`,`AwayTeamID`),
  ADD KEY `FK_MATCH_AYearATeamID` (`AwayYear`,`AwayTeamID`);

--
-- Indexes for table `MEMBER`
--
ALTER TABLE `MEMBER`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `PLAYER`
--
ALTER TABLE `PLAYER`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `FK_PLAYER_HomeClubName` (`HomeClubName`);

--
-- Indexes for table `POOLGAME`
--
ALTER TABLE `POOLGAME`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `SAVES`
--
ALTER TABLE `SAVES`
  ADD PRIMARY KEY (`PlayerID`,`MatchID`),
  ADD KEY `FK_SAVES_MatchID` (`MatchID`);

--
-- Indexes for table `SUPPORTSTAFF`
--
ALTER TABLE `SUPPORTSTAFF`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `TEAM`
--
ALTER TABLE `TEAM`
  ADD PRIMARY KEY (`Year`,`ID`),
  ADD KEY `FK_TEAM_Country` (`Country`);

--
-- Indexes for table `TEAMMEMBER`
--
ALTER TABLE `TEAMMEMBER`
  ADD PRIMARY KEY (`Year`,`TeamID`,`MemberID`),
  ADD KEY `FK_TEAMMEMBER_MemberID` (`MemberID`);

--
-- Indexes for table `TICKET`
--
ALTER TABLE `TICKET`
  ADD PRIMARY KEY (`MatchID`,`Ticket#`),
  ADD KEY `CustomerID` (`CustomerID`);

--
-- Indexes for table `TOURNAMENT`
--
ALTER TABLE `TOURNAMENT`
  ADD PRIMARY KEY (`Year`),
  ADD KEY `FK_Tournament_country` (`Country`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `ELIMINATIONGAME`
--
ALTER TABLE `ELIMINATIONGAME`
  ADD CONSTRAINT `FK_ELIMINATIONGAME_ID` FOREIGN KEY (`ID`) REFERENCES `MATCH` (`ID`) ON DELETE CASCADE;

--
-- Constraints for table `GOALS`
--
ALTER TABLE `GOALS`
  ADD CONSTRAINT `FK_GOALS_MatchID` FOREIGN KEY (`MatchID`) REFERENCES `MATCH` (`ID`) ON DELETE CASCADE,
  ADD CONSTRAINT `FK_GOALS_PlayerID` FOREIGN KEY (`PlayerID`) REFERENCES `PLAYER` (`ID`) ON DELETE CASCADE;

--
-- Constraints for table `HOMECLUB`
--
ALTER TABLE `HOMECLUB`
  ADD CONSTRAINT `FK_HOMECLUB_Country` FOREIGN KEY (`Country`) REFERENCES `COUNTRY` (`Name`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `MATCH`
--
ALTER TABLE `MATCH`
  ADD CONSTRAINT `FK_MATCH_AYearATeamID` FOREIGN KEY (`AwayYear`,`AwayTeamID`) REFERENCES `TEAM` (`Year`, `ID`) ON DELETE CASCADE,
  ADD CONSTRAINT `FK_MATCH_HYearHTeamID` FOREIGN KEY (`HomeYear`,`HomeTeamID`) REFERENCES `TEAM` (`Year`, `ID`) ON DELETE CASCADE;

--
-- Constraints for table `PLAYER`
--
ALTER TABLE `PLAYER`
  ADD CONSTRAINT `FK_PLAYER_HomeClubName` FOREIGN KEY (`HomeClubName`) REFERENCES `HOMECLUB` (`Name`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_PLAYER_ID` FOREIGN KEY (`ID`) REFERENCES `MEMBER` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `POOLGAME`
--
ALTER TABLE `POOLGAME`
  ADD CONSTRAINT `FK_POOLGAME_ID` FOREIGN KEY (`ID`) REFERENCES `MATCH` (`ID`) ON DELETE CASCADE;

--
-- Constraints for table `SAVES`
--
ALTER TABLE `SAVES`
  ADD CONSTRAINT `FK_SAVES_MatchID` FOREIGN KEY (`MatchID`) REFERENCES `MATCH` (`ID`) ON DELETE CASCADE,
  ADD CONSTRAINT `FK_SAVES_PlayerID` FOREIGN KEY (`PlayerID`) REFERENCES `PLAYER` (`ID`) ON DELETE CASCADE;

--
-- Constraints for table `SUPPORTSTAFF`
--
ALTER TABLE `SUPPORTSTAFF`
  ADD CONSTRAINT `FK_SUPPORTSTAFF_ID` FOREIGN KEY (`ID`) REFERENCES `MEMBER` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `TEAM`
--
ALTER TABLE `TEAM`
  ADD CONSTRAINT `FK_TEAM_Country` FOREIGN KEY (`Country`) REFERENCES `COUNTRY` (`Name`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_TEAM_Year` FOREIGN KEY (`Year`) REFERENCES `TOURNAMENT` (`Year`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `TEAMMEMBER`
--
ALTER TABLE `TEAMMEMBER`
  ADD CONSTRAINT `FK_TEAMMEMBER_MemberID` FOREIGN KEY (`MemberID`) REFERENCES `MEMBER` (`ID`) ON DELETE CASCADE,
  ADD CONSTRAINT `FK_TEAMMEMBER_YearTeamID` FOREIGN KEY (`Year`,`TeamID`) REFERENCES `TEAM` (`Year`, `ID`) ON DELETE CASCADE;

--
-- Constraints for table `TICKET`
--
ALTER TABLE `TICKET`
  ADD CONSTRAINT `FK_TICKET_CustomerID` FOREIGN KEY (`CustomerID`) REFERENCES `CUSTOMER` (`ID`) ON DELETE CASCADE,
  ADD CONSTRAINT `FK_TICKET_MatchID` FOREIGN KEY (`MatchID`) REFERENCES `MATCH` (`ID`) ON DELETE CASCADE;

--
-- Constraints for table `TOURNAMENT`
--
ALTER TABLE `TOURNAMENT`
  ADD CONSTRAINT `FK_Tournament_country` FOREIGN KEY (`Country`) REFERENCES `COUNTRY` (`Name`) ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

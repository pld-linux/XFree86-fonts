
%define		_sver	%(echo %{version} | tr -d .)
%define		_prefix		/usr/X11R6

Summary:	XFree86 Fonts
Summary(pl):	Fonty dla systemu XFree86
Name:		XFree86-fonts
Version:	4.2.0
Release:	5.1
License:	MIT
Group:		X11/XFree86
Source0:	ftp://ftp.xfree86.org/pub/XFree86/%{version}/source/X%{_sver}src-2.tgz
Source1:	ftp://ftp.xfree86.org/pub/XFree86/%{version}/source/X%{_sver}src-1.tgz
Source2:	http://www.biz.net.pl/images/ISO8859-2-bdf.tar.gz
Source3:	ftp://crash.fce.vutbr.cz/pub/linux_fonts/TGZ/ulT1mo-beta-1.0.tgz
Source4:	%{name}.Fontmap
Source5:	%{name}-latin2-Type1.Fontmap
Source6:	vga.pcf
Patch0:		%{name}-extras-fix.patch
Patch1:		%{name}-ISO8859-2.patch
Patch2:		%{name}-do_not_run_xftchache.patch
BuildRequires:	XFree86 >= %{version}-0.8
BuildRequires:	XFree86-devel >= %{version}-0.8
BuildRequires:	perl
BuildRequires:	t1utils
Requires(post):	%{_bindir}/mkfontdir
Requires(post):	fileutils
Requires(post):	textutils
Requires(post):	sed
Requires(postun):	%{_bindir}/mkfontdir
Requires(postun):	fileutils
Requires(postun):	textutils
Requires(postun):	sed
Requires:	%{name}-base = %{version}
Obsoletes:	XFree86-latin2-fonts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_mandir		%{_prefix}/man
%define		_t1fontsdir	%{_fontsdir}/Type1
%define		_t1afmdir	%{_t1fontsdir}/afm
%define		_t1pfmdir	%{_t1fontsdir}/pfm

%description
This package contains the basic fonts. This package is required when
you have installed X server.

%description -l pl
Pakiet ten zawiera podstawowe czcionki. Pakiet ten jest koniecznie
potrzebny, je¶li masz zainstalowany jakikolwiek X serwer.

%package utils
Summary:	Perl scripts for generating BDF fonts
Summary(pl):	Skrypty perlowe do generowania fontów BDF
Group:		X11/XFree86

%description utils
Perl scripts that allow to generate from an ISO10646-1 encoded BDF
font other BDF fonts in any possible encoding.

%description utils -l pl
Skrypty perlowe pozwalaj±ce wygenerowaæ z fontów BDF kodowanych w
ISO10646-1 fonty BDF z dowolnym kodowaniem.

%package base
Summary:	Base fonts (cursor and fixed)
Summary(pl):	Podstawowe fonty (cursor i fixed)
Group:		X11/XFree86

%description base
Base fonts (cursor and fixed) needed to start X server.

%description base -l pl
Podstawowe fonty (cursor i fixed) niezbêdne do uruchomienia X serwera.

%package PEX
Summary:	PEX fonts
Summary(pl):	Fonty PEX
Group:		X11/XFree86

%description PEX
PEX fonts for PEX extension (not installed by default since 4.2.0).

%description PEX -l pl
Fonty PEX do rozszerzenia PEX (nie instalowane domy¶lnie od 4.2.0).

%package 75dpi
Summary:	X11R6 75dpi fonts - only need on server side
Summary(de):	X11RT 75 dpi-Fonts - nur auf Serverseite erforderlich
Summary(fr):	Fontes 75 dpi X11R6 - nécessaire uniquement côté serveur
Summary(pl):	Fonty o rozdzielczo¶ci 75dpi - potrzebne tylko po stronie serwera
Summary(tr):	X11R6 75dpi yazýtipleri - yalnýzca sunucu tarafýnda gerekir
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir
Obsoletes:	XFree86-75dpi-fonts
%ifarch sparc
Obsoletes:	X11R6.1-75dpi-fonts
%endif

%description 75dpi
The 75dpi fonts used on most Linux systems. Users with high resolution
displays may prefer the 100dpi fonts available in a separate package.

%description 75dpi -l de
Die 75dpi-Fonts, die auf meisten Linux-Systemen verwendet werden. Für
Benutzer mit einer hochauflösender Darstellung sind die 100dpi-Fonts
eines getrennt erhältlichen Pakets besser geeignet.

%description 75dpi -l fr
Fontes 75 dpi utilisées sur la plupart des systèmes Linux. Ceux qui
ont des écrans à haute résolution préfèreront les fontes 100 dpi
disponibles dans un autre paquetage.

%description 75dpi -l pl
Pakiet ten zawiera czcionki rastrowe 75dpi. W wypadku wiêkszej
rozdzielczo¶ci zalecane s± czcionki 100dpi, które s± dostêpne w
osobnym pakiecie.

%description 75dpi -l tr
Çoðu Linux sisteminde 75dpi yazýtipi kullanýlýr. Yüksek çözünürlük
kullanan kullanýcýlar 100dpi yazýtiplerini yeðleyebilirler.

%package 100dpi
Summary:	X11R6 100dpi fonts - only need on server side
Summary(de):	X11R6 100dpi-Fonts - nur auf Server-Seite erforderlich
Summary(fr):	Fontes 100ppp pour X11R6 - nécessaires seulement coté serveur.
Summary(pl):	Fonty o rozdzielczosci 100dpi - potrzebne tylko po stronie serwera
Summary(tr):	X11R6 100dpi yazýtipleri - yalnýzca sunucu tarafýnda gereklidir
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir
Obsoletes:	XFree86-100dpi-fonts

%ifarch sparc
Obsoletes:	X11R6.1-100dpi-fonts
%endif

%description 100dpi
The 100dpi fonts used on most Linux systems. Users with high
resolution displays may prefer the 100dpi fonts available in a
separate package.

%description 100dpi -l de
Die 100dpi-Schriftarten, die auf den meisten Linux-Systemen zum
Einsatz kommen. Anwender mit hochauflösenden Monitoren ziehen unter
Umständen die 100dpi-Schriften vor, die in einem separaten Paket
erhältlich sind.

%description 100dpi -l fr
Les fontes 100dpi sont utilisées par la plupart des systèmes Linux.
Les utilisateurs ayant des hautes résolutions peuvent préférer les
fontes 100dpi disponibles dans un package séparé.

%description 100dpi -l pl
Pakiet ten zawiera czcionki rastrowe 100dpi. Bed± one potrzebne przy
pracy w du¿ych rozdzielczo¶ciach.

%description 100dpi -l tr
Yüksek çözünürlük kullanan kullanýcýlar 100dpi yazýtiplerini 75dpi
olanlara yeðleyebilirler.

%package KOI8-R
Summary:	KOI8-R (cyrillic) fonts - only need on server side
Summary(pl):	Fonty rastrowe KOI8-R (cyrylica)
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir
Obsoletes:	XFree86-cyrillic-fonts

%description KOI8-R
KOI8-R (cyrillic) raster fonts.

%description KOI8-R -l pl
Fonty rastrowe KOI8-R (cyrylica).

%package 100dpi-KOI8-R
Summary:	KOI8-R 100dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe KOI8-R o rozdzielczo¶ci 100dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 100dpi-KOI8-R
KOI8-R raster fonts.

%description 100dpi-KOI8-R -l pl
Fonty rastrowe KOI8-R o rozdzielczo¶ci 100dpi.

%package 75dpi-KOI8-R
Summary:	KOI8-R 75dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe KOI8-R o rozdzielczo¶ci 75dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 75dpi-KOI8-R
KOI8-R raster fonts.

%description 75dpi-KOI8-R -l pl
Fonty rastrowe ISO-KOI8-R o rozdzielczo¶ci 75dpi.

%package ISO8859-1
Summary:	ISO-8859-1 basic fonts - only need on server side
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-1
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description ISO8859-1
Basic ISO-8859-1 raster fonts.

%description ISO8859-1 -l pl
Podstawowe fonty rastrowe ISO-8859-1.

%package 100dpi-ISO8859-1
Summary:	ISO-8859-1 100dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-1 o rozdzielczo¶ci 100dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 100dpi-ISO8859-1
ISO-8859-1 raster fonts.

%description 100dpi-ISO8859-1 -l pl
Fonty rastrowe ISO-8859-1 o rozdzielczo¶ci 100dpi.

%package 75dpi-ISO8859-1
Summary:	ISO-8859-1 75dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-1 o rozdzielczo¶ci 75dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 75dpi-ISO8859-1
ISO-8859-1 raster fonts.

%description 75dpi-ISO8859-1 -l pl
Fonty rastrowe ISO-8859-1 o rozdzielczo¶ci 75dpi.

%package ISO8859-2
Summary:	ISO-8859-2 basic fonts - only need on server side
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-2
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description ISO8859-2
Basic ISO-8859-2 raster fonts.

%description ISO8859-2 -l pl
Podstawowe fonty rastrowe ISO-8859-2.

%package 100dpi-ISO8859-2
Summary:	ISO-8859-2 100dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-2 o rozdzielczo¶ci 100dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir
Obsoletes:	XFree86-ISO8859-2-100dpi-fonts
Obsoletes:	XFree86-latin2-100dpi-fonts

%description 100dpi-ISO8859-2
ISO-8859-2 raster fonts.

%description 100dpi-ISO8859-2 -l pl
Fonty rastrowe ISO-8859-2 o rozdzielczo¶ci 100dpi.

%package 75dpi-ISO8859-2
Summary:	ISO-8859-2 75dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-2 o rozdzielczo¶ci 75dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir
Obsoletes:	XFree86-ISO8859-2-75dpi-fonts
Obsoletes:	XFree86-latin2-75dpi-fonts

%description 75dpi-ISO8859-2
ISO-8859-2 raster fonts.

%description 75dpi-ISO8859-2 -l pl
Fonty rastrowe ISO-8859-2 o rozdzielczo¶ci 75dpi.

%package Type1-ISO8859-2
Summary:	Type1 (scalable) ISO8859-2 X11 system fonts
Summary(pl):	Fonty Type 1 ISO-8859-2
Group:		X11/Fonts
Requires(post):	fileutils
Requires(post):	grep
Requires(post):	textutils
Requires(post):	sed
Requires(postun):	fileutils
Requires(postun):	grep
Requires(postun):	textutils
Requires(postun):	sed
Requires:	XFree86 > 3.2
Obsoletes:	XFree86-ISO8859-2-Type1-fonts
Obsoletes:	XFree86-latin2-Type1-fonts

%description Type1-ISO8859-2
This package includes the Central European (ISO-8859-2) Type1 fonts
for the X11 system.

This is the famous ulT1mo (read ultimo) collection. All fonts are
copyrighted to their authors and declared to be freeware. Originals
was taken from the net or CDs.

%description Type1-ISO8859-2 -l pl
Pakiet ten zawiera zestaw fontów Type1 ISO-8859-2 dla X Window.

%package ISO8859-3
Summary:	ISO-8859-3 basic fonts - only need on server side
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-3
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description ISO8859-3
Basic ISO-8859-3 raster fonts.

%description ISO8859-3 -l pl
Podstawowe fonty rastrowe ISO-8859-3.

%package 100dpi-ISO8859-3
Summary:	ISO-8859-3 100dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-3 o rozdzielczo¶ci 100dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 100dpi-ISO8859-3
ISO-8859-3 raster fonts.

%description 100dpi-ISO8859-3 -l pl
Fonty rastrowe ISO-8859-3 o rozdzielczo¶ci 100dpi.

%package 75dpi-ISO8859-3
Summary:	ISO-8859-3 75dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-3 o rozdzielczo¶ci 75dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 75dpi-ISO8859-3
ISO-8859-3 raster fonts.

%description 75dpi-ISO8859-3 -l pl
Fonty rastrowe ISO-8859-3 o rozdzielczo¶ci 75dpi.

%package ISO8859-4
Summary:	ISO-8859-4 basic fonts - only need on server side
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-4
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description ISO8859-4
Basic ISO-8859-4 raster fonts.

%description ISO8859-4 -l pl
Podstawowe fonty rastrowe ISO-8859-4.

%package 100dpi-ISO8859-4
Summary:	ISO-8859-4 100dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-4 o rozdzielczo¶ci 100dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 100dpi-ISO8859-4
ISO-8859-4 raster fonts.

%description 100dpi-ISO8859-4 -l pl
Fonty rastrowe ISO-8859-4 o rozdzielczo¶ci 100dpi.

%package 75dpi-ISO8859-4
Summary:	ISO-8859-4 75dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-4 o rozdzielczo¶ci 75dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 75dpi-ISO8859-4
ISO-8859-4 raster fonts.

%description 75dpi-ISO8859-4 -l pl
Fonty rastrowe ISO-8859-4 o rozdzielczo¶ci 75dpi.

%package ISO8859-5
Summary:	ISO-8859-5 basic fonts - only need on server side
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-5
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description ISO8859-5
Basic ISO-8859-5 raster fonts.

%description ISO8859-5 -l pl
Podstawowe fonty rastrowe ISO-8859-5.

%package 100dpi-ISO8859-5
Summary:	ISO-8859-5 100dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-5 o rozdzielczo¶ci 100dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 100dpi-ISO8859-5
ISO-8859-5 raster fonts.

%description 100dpi-ISO8859-5 -l pl
Fonty rastrowe ISO-8859-5 o rozdzielczo¶ci 100dpi.

%package 75dpi-ISO8859-5
Summary:	ISO-8859-5 75dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-5 o rozdzielczo¶ci 75dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 75dpi-ISO8859-5
ISO-8859-5 raster fonts.

%description 75dpi-ISO8859-5 -l pl
Fonty rastrowe ISO-8859-5 o rozdzielczo¶ci 75dpi.

%package ISO8859-6
Summary:	ISO-8859-6 basic fonts - only need on server side
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-6
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description ISO8859-6
Basic ISO-8859-6 raster fonts.

%description ISO8859-6 -l pl
Podstawowe fonty rastrowe ISO-8859-6.

%package 100dpi-ISO8859-6
Summary:	ISO-8859-6 100dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-6 o rozdzielczo¶ci 100dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 100dpi-ISO8859-6
ISO-8859-6 raster fonts.

%description 100dpi-ISO8859-6 -l pl
Fonty rastrowe ISO-8859-6 o rozdzielczo¶ci 100dpi.

%package 75dpi-ISO8859-6
Summary:	ISO-8859-6 75dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-6 o rozdzielczo¶ci 75dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 75dpi-ISO8859-6
ISO-8859-6 raster fonts.

%description 75dpi-ISO8859-6 -l pl
Fonty rastrowe ISO-8859-6 o rozdzielczo¶ci 75dpi.

%package ISO8859-7
Summary:	ISO-8859-7 basic fonts - only need on server side
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-7
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description ISO8859-7
Basic ISO-8859-7 raster fonts.

%description ISO8859-7 -l pl
Podstawowe fonty rastrowe ISO-8859-7.

%package 100dpi-ISO8859-7
Summary:	ISO-8859-7 100dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-7 o rozdzielczo¶ci 100dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 100dpi-ISO8859-7
ISO-8859-7 raster fonts.

%description 100dpi-ISO8859-7 -l pl
Fonty rastrowe ISO-8859-7 o rozdzielczo¶ci 100dpi.

%package 75dpi-ISO8859-7
Summary:	ISO-8859-7 75dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-7 o rozdzielczo¶ci 75dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 75dpi-ISO8859-7
ISO-8859-7 raster fonts.

%description 75dpi-ISO8859-7 -l pl
Fonty rastrowe ISO-8859-7 o rozdzielczo¶ci 75dpi.

%package ISO8859-8
Summary:	ISO-8859-8 basic fonts - only need on server side
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-8
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description ISO8859-8
Basic ISO-8859-8 raster fonts.

%description ISO8859-8 -l pl
Podstawowe fonty rastrowe ISO-8859-8.

%package 100dpi-ISO8859-8
Summary:	ISO-8859-8 100dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-8 o rozdzielczo¶ci 100dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 100dpi-ISO8859-8
ISO-8859-8 raster fonts.

%description 100dpi-ISO8859-8 -l pl
Fonty rastrowe ISO-8859-8 o rozdzielczo¶ci 100dpi.

%package 75dpi-ISO8859-8
Summary:	ISO-8859-8 75dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-8 o rozdzielczo¶ci 75dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 75dpi-ISO8859-8
ISO-8859-8 raster fonts.

%description 75dpi-ISO8859-8 -l pl
Fonty rastrowe ISO-8859-8 o rozdzielczo¶ci 75dpi.

%package ISO8859-9
Summary:	ISO-8859-9 basic fonts - only need on server side
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-9
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description ISO8859-9
Basic ISO-8859-9 raster fonts.

%description ISO8859-9 -l pl
Podstawowe fonty rastrowe ISO-8859-9.

%package 100dpi-ISO8859-9
Summary:	ISO-8859-9 100dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-9 o rozdzielczo¶ci 100dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 100dpi-ISO8859-9
ISO-8859-9 raster fonts.

%description 100dpi-ISO8859-9 -l pl
Fonty rastrowe ISO-8859-9 o rozdzielczo¶ci 100dpi.

%package 75dpi-ISO8859-9
Summary:	ISO-8859-9 75dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-9 o rozdzielczo¶ci 75dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 75dpi-ISO8859-9
ISO-8859-9 raster fonts.

%description 75dpi-ISO8859-9 -l pl
Fonty rastrowe ISO-8859-9 o rozdzielczo¶ci 75dpi.

%package ISO8859-10
Summary:	ISO-8859-10 basic fonts - only need on server side
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-10
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description ISO8859-10
Basic ISO-8859-10 raster fonts.

%description ISO8859-10 -l pl
Podstawowe fonty rastrowe ISO-8859-10.

%package 100dpi-ISO8859-10
Summary:	ISO-8859-10 100dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-10 o rozdzielczo¶ci 100dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 100dpi-ISO8859-10
ISO-8859-10 raster fonts.

%description 100dpi-ISO8859-10 -l pl
Fonty rastrowe ISO-8859-10 o rozdzielczo¶ci 100dpi.

%package 75dpi-ISO8859-10
Summary:	ISO-8859-10 75dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-10 o rozdzielczo¶ci 75dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 75dpi-ISO8859-10
ISO-8859-10 raster fonts.

%description 75dpi-ISO8859-10 -l pl
Fonty rastrowe ISO-8859-10 o rozdzielczo¶ci 75dpi.

%package ISO8859-11
Summary:	ISO-8859-11 basic fonts - only need on server side
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-11
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description ISO8859-11
Basic ISO-8859-11 raster fonts.

%description ISO8859-11 -l pl
Podstawowe fonty rastrowe ISO-8859-11.

%package 100dpi-ISO8859-11
Summary:	ISO-8859-11 100dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-11 o rozdzielczo¶ci 100dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 100dpi-ISO8859-11
ISO-8859-11 raster fonts.

%description 100dpi-ISO8859-11 -l pl
Fonty rastrowe ISO-8859-11 o rozdzielczo¶ci 100dpi.

%package 75dpi-ISO8859-11
Summary:	ISO-8859-11 75dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-11 o rozdzielczo¶ci 75dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 75dpi-ISO8859-11
ISO-8859-11 raster fonts.

%description 75dpi-ISO8859-11 -l pl
Fonty rastrowe ISO-8859-11 o rozdzielczo¶ci 75dpi.

%package ISO8859-12
Summary:	ISO-8859-12 basic fonts - only need on server side
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-12
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description ISO8859-12
Basic ISO-8859-12 raster fonts.

%description ISO8859-12 -l pl
Podstawowe fonty rastrowe ISO-8859-12.

%package 100dpi-ISO8859-12
Summary:	ISO-8859-12 100dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-12 o rozdzielczo¶ci 100dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 100dpi-ISO8859-12
ISO-8859-12 raster fonts.

%description 100dpi-ISO8859-12 -l pl
Fonty rastrowe ISO-8859-12 o rozdzielczo¶ci 100dpi.

%package 75dpi-ISO8859-12
Summary:	ISO-8859-12 75dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-12 o rozdzielczo¶ci 75dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 75dpi-ISO8859-12
ISO-8859-12 raster fonts.

%description 75dpi-ISO8859-12 -l pl
Fonty rastrowe ISO-8859-12 o rozdzielczo¶ci 75dpi.

%package ISO8859-13
Summary:	ISO-8859-13 basic fonts - only need on server side
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-13
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description ISO8859-13
Basic ISO-8859-13 raster fonts.

%description ISO8859-13 -l pl
Podstawowe fonty rastrowe ISO-8859-13.

%package 100dpi-ISO8859-13
Summary:	ISO-8859-13 100dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-13 o rozdzielczo¶ci 100dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 100dpi-ISO8859-13
ISO-8859-13 raster fonts.

%description 100dpi-ISO8859-13 -l pl
Fonty rastrowe ISO-8859-13 o rozdzielczo¶ci 100dpi.

%package 75dpi-ISO8859-13
Summary:	ISO-8859-13 75dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-13 o rozdzielczo¶ci 75dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 75dpi-ISO8859-13
ISO-8859-13 raster fonts.

%description 75dpi-ISO8859-13 -l pl
Fonty rastrowe ISO-8859-13 o rozdzielczo¶ci 75dpi.

%package ISO8859-14
Summary:	ISO-8859-14 basic fonts - only need on server side
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-14
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description ISO8859-14
Basic ISO-8859-14 raster fonts.

%description ISO8859-14 -l pl
Podstawowe fonty rastrowe ISO-8859-14.

%package 100dpi-ISO8859-14
Summary:	ISO-8859-14 100dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-14 o rozdzielczo¶ci 100dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 100dpi-ISO8859-14
ISO-8859-14 raster fonts.

%description 100dpi-ISO8859-14 -l pl
Fonty rastrowe ISO-8859-14 o rozdzielczo¶ci 100dpi.

%package 75dpi-ISO8859-14
Summary:	ISO-8859-14 75dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-14 o rozdzielczo¶ci 75dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 75dpi-ISO8859-14
ISO-8859-14 raster fonts.

%description 75dpi-ISO8859-14 -l pl
Fonty rastrowe ISO-8859-14 o rozdzielczo¶ci 75dpi.

%package ISO8859-15
Summary:	ISO-8859-15 basic fonts - only need on server side
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-15
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description ISO8859-15
Basic ISO-8859-15 raster fonts.

%description ISO8859-15 -l pl
Podstawowe fonty rastrowe ISO-8859-15.

%package 100dpi-ISO8859-15
Summary:	ISO-8859-15 100dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-15 o rozdzielczo¶ci 100dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 100dpi-ISO8859-15
ISO-8859-15 raster fonts.

%description 100dpi-ISO8859-15 -l pl
Fonty rastrowe ISO-8859-15 o rozdzielczo¶ci 100dpi.

%package 75dpi-ISO8859-15
Summary:	ISO-8859-15 75dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-15 o rozdzielczo¶ci 75dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 75dpi-ISO8859-15
ISO-8859-15 raster fonts.

%description 75dpi-ISO8859-15 -l pl
Fonty rastrowe ISO-8859-15 o rozdzielczo¶ci 75dpi.

%package JISX0201.1976-0
Summary:	JISX0201.1976-0 basic fonts - only need on server side
Summary(pl):	Podstawowe fonty rastrowe JISX0201.1976-0
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description JISX0201.1976-0
Basic JISX0201.1976-0 raster fonts.

%description JISX0201.1976-0 -l pl
Podstawowe fonty rastrowe JISX0201.1976-0.

%package 100dpi-JISX0201.1976-0
Summary:	JISX0201.1976-0 100dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe JISX0201.1976-0 o rozdzielczo¶ci 100dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 100dpi-JISX0201.1976-0
JISX0201.1976-0 raster fonts.

%description 100dpi-JISX0201.1976-0 -l pl
Fonty rastrowe JISX0201.1976-0 o rozdzielczo¶ci 100dpi.

%package 75dpi-JISX0201.1976-0
Summary:	JISX0201.1976-0 75dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe JISX0201.1976-0 o rozdzielczo¶ci 75dpi
Group:		X11/XFree86
Requires(post):	%{_bindir}/mkfontdir
Requires(postun):	%{_bindir}/mkfontdir

%description 75dpi-JISX0201.1976-0
JISX0201.1976-0 raster fonts.

%description 75dpi-JISX0201.1976-0 -l pl
Fonty rastrowe JISX0201.1976-0 o rozdzielczo¶ci 75dpi.

%prep
%setup -q -c -a1 -a2 -a3
%patch0 -p1
%patch1 -p1
%patch2 -p1

cp -f xc/extras/fonts/arabic24/*.bdf xc/fonts/bdf/misc
cp -f xc/extras/fonts/ClearlyU/*.bdf xc/fonts/bdf/misc

# move ISO8859-2 fonts to main tree
for i in {misc/{12x24,8x16},{75,100}dpi/{char,term,lu{BIS,bB}19}}*.bdf ; do
	j="`echo $i | sed 's/\.bdf$//'`-ISO8859-2.bdf"
	mv -f $i xc/fonts/bdf/$j
done

%build
%{__make} all -C ulT1mo-beta-1.0

cd xc/fonts
imake -DBuildFonts -DUseInstalled -I%{_libdir}/X11/config
%{__make} Makefiles
%{__make} depend
cd ..
%{__make} -C fonts TOP=`pwd` \
	UCS2ANY=`pwd`/fonts/util/ucs2any.pl \
	BDFTRUNCATE=`pwd`/fonts/util/bdftruncate.pl \
	UCSMAPPREFIX=`pwd`/fonts/util/map- \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
cd xc
%{__make} -C fonts install TOP=`pwd` \
	UCS2ANY=`pwd`/fonts/util/ucs2any.pl \
	BDFTRUNCATE=`pwd`/fonts/util/bdftruncate.pl \
	UCSMAPPREFIX=`pwd`/fonts/util/map- \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} -C fonts install.man TOP=`pwd` \
	UCS2ANY=`pwd`/fonts/util/ucs2any.pl \
	BDFTRUNCATE=`pwd`/fonts/util/bdftruncate.pl \
	UCSMAPPREFIX=`pwd`/fonts/util/map- \
	DESTDIR=$RPM_BUILD_ROOT
cd ..

%{__make} -C ulT1mo-beta-1.0 install \
	FONTDIR=$RPM_BUILD_ROOT%{_fontsdir}

# separate *.afm, convert *.pfa to .pfb
mv -f $RPM_BUILD_ROOT%{_t1fontsdir}/*.afm $RPM_BUILD_ROOT%{_t1afmdir}
(cd $RPM_BUILD_ROOT%{_t1fontsdir}
for f in *.pfa ; do
	t1binary $f `basename $f .pfa`.pfb
	rm -f $f
done
)

# make "fixed" font
#sed -e 's/^FONT -Misc.*/FONT fixed/' xc/fonts/bdf/misc/6x13-ISO8859-1.bdf | \
#	%{_bindir}/bdftopcf -t | gzip -9 > $RPM_BUILD_ROOT%{_fontsdir}/misc/fixed.pcf.gz

# split fonts.alias (separate "fixed")
grep -v '^fixed[ \t]' $RPM_BUILD_ROOT%{_fontsdir}/misc/fonts.alias \
	> $RPM_BUILD_ROOT%{_fontsdir}/misc/fonts.alias.10XFree86-fonts
grep '^fixed[ \t].*' $RPM_BUILD_ROOT%{_fontsdir}/misc/fonts.alias \
	> $RPM_BUILD_ROOT%{_fontsdir}/misc/fonts.alias.00XFree86-fonts-base
rm -f $RPM_BUILD_ROOT%{_fontsdir}/misc/fonts.alias
	
tail -n +2 ulT1mo-beta-1.0/fonts.scale.ulT1mo | sed -e 's/\.pfb/-ISO-8859-2\.pfb/' \
	> $RPM_BUILD_ROOT%{_t1fontsdir}/fonts.scale.XFree86-fonts-Type1-ISO8859-2
tail -n +2 xc/fonts/scaled/Type1/fonts.scale | sed -e 's/\.pfa/\.pfb/' \
	> $RPM_BUILD_ROOT%{_t1fontsdir}/fonts.scale.%{name}
install %{SOURCE4} $RPM_BUILD_ROOT%{_t1fontsdir}/Fontmap.%{name}
install %{SOURCE5} $RPM_BUILD_ROOT%{_t1fontsdir}/Fontmap.XFree86-fonts-Type1-ISO8859-2
install %{SOURCE6} $RPM_BUILD_ROOT%{_fontsdir}/misc
tail -n +2 $RPM_BUILD_ROOT%{_fontsdir}/TTF/fonts.scale \
	> $RPM_BUILD_ROOT%{_fontsdir}/TTF/fonts.scale.XFree86-fonts
rm -f $RPM_BUILD_ROOT%{_fontsdir}/TTF/fonts.scale
gzip -9nf $RPM_BUILD_ROOT%{_fontsdir}/misc/vga.pcf

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_fontsdir}/misc
umask 022
cat fonts.alias.* > fonts.alias
%{_bindir}/mkfontdir
cd %{_t1fontsdir}
rm -f fonts.scale.bak Fontmap.bak
cat fonts.scale.* | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp
ln -sf fonts.scale fonts.dir
cat Fontmap.* > Fontmap
if [ -x %{_bindir}/xftcache ]; then
	%{_bindir}/xftcache .
fi
cd %{_fontsdir}/TTF
umask 022
cat fonts.scale.* | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp
ln -sf fonts.scale fonts.dir
if [ -x %{_bindir}/xftcache ]; then
	%{_bindir}/xftcache .
fi

%postun
cd %{_fontsdir}/misc
umask 022
cat fonts.alias.* > fonts.alias 2>/dev/null
%{_bindir}/mkfontdir
cd %{_t1fontsdir}
rm -f fonts.scale.bak Fontmap.bak
cat fonts.scale.* 2>/dev/null | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp
ln -sf fonts.scale fonts.dir
cat Fontmap.* > Fontmap 2>/dev/null
if [ -x %{_bindir}/xftcache ]; then
	%{_bindir}/xftcache .
fi
cd %{_fontsdir}/TTF
umask 022
cat fonts.scale.* | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp
ln -sf fonts.scale fonts.dir
if [ -x %{_bindir}/xftcache ]; then
	%{_bindir}/xftcache .
fi

%post base
cd %{_fontsdir}/misc
umask 022
cat fonts.alias.* > fonts.alias
if [ -x %{_bindir}/mkfontdir ]; then
	%{_bindir}/mkfontdir
else
	cat > fonts.dir <<EOF
2
6x13-ISO8859-1.pcf.gz -misc-fixed-medium-r-semicondensed--13-120-75-75-c-60-iso8859-1
cursor.pcf.gz cursor
EOF
fi

%postun base
cd %{_fontsdir}/misc
umask 022
cat fonts.alias.* > fonts.alias 2>/dev/null
if [ -x %{_bindir}/mkfontdir ]; then
	%{_bindir}/mkfontdir
else
	:> fonts.dir
fi

%post 75dpi
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%postun 75dpi
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%post 100dpi
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%postun 100dpi
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%post ISO8859-1
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%postun ISO8859-1
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%post 75dpi-ISO8859-1
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%postun 75dpi-ISO8859-1
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%post 100dpi-ISO8859-1
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%postun 100dpi-ISO8859-1
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%post ISO8859-2
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%postun ISO8859-2
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%post 75dpi-ISO8859-2
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%postun 75dpi-ISO8859-2
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%post 100dpi-ISO8859-2
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%postun 100dpi-ISO8859-2
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%post Type1-ISO8859-2
cd %{_t1fontsdir}
rm -f fonts.scale.bak Fontmap.bak
cat fonts.scale.* | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp
ln -sf fonts.scale fonts.dir
cat Fontmap.* > Fontmap
grep '^.*ISO-8859-2.pfb' %{_t1fontsdir}/fonts.dir |\
	sed 's/\(^.*ISO-8859-2.pfb \)\(.*\)/"\2"/' |\
	sed 's/\(^".*\)\(-[a-z]*-[a-z]*"\)/\1-iso8859-2" \1\2/' |\
	grep -v ^[0-9] > %{_t1fontsdir}/fonts.alias.tmp
cat %{_t1fontsdir}/fonts.alias.tmp >> %{_t1fontsdir}/fonts.alias
sort -u < %{_t1fontsdir}/fonts.alias > %{_t1fontsdir}/fonts.alias.tmp
mv -f %{_t1fontsdir}/fonts.alias.tmp %{_t1fontsdir}/fonts.alias
if [ -x %{_bindir}/xftcache ]; then
	%{_bindir}/xftcache .
fi

%postun Type1-ISO8859-2
cd %{_t1fontsdir}
rm -f fonts.scale.bak Fontmap.bak
cat fonts.scale.* 2>/dev/null | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp
ln -sf fonts.scale fonts.dir
cat Fontmap.* > Fontmap 2>/dev/null
sed 's/^.*pfb -//' %{_t1fontsdir}/fonts.dir > %{_t1fontsdir}/fonts.dir.tmp
grep -f %{_t1fontsdir}/fonts.dir.tmp \
	%{_t1fontsdir}/fonts.alias > %{_t1fontsdir}/fonts.alias.tmp
mv -f %{_t1fontsdir}/fonts.alias.tmp %{_t1fontsdir}/fonts.alias
rm -f %{_t1fontsdir}/fonts.dir.tmp
if [ -x %{_bindir}/xftcache ]; then
	%{_bindir}/xftcache .
fi

%post ISO8859-3
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%postun ISO8859-3
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%post 75dpi-ISO8859-3
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%postun 75dpi-ISO8859-3
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%post 100dpi-ISO8859-4
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%postun 100dpi-ISO8859-4
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%post ISO8859-5
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%postun ISO8859-5
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%post 75dpi-ISO8859-5
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%postun 75dpi-ISO8859-5
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%post 100dpi-ISO8859-5
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%postun 100dpi-ISO8859-5
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%post ISO8859-6
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%postun ISO8859-6
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%post 75dpi-ISO8859-6
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%postun 75dpi-ISO8859-6
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%post 100dpi-ISO8859-6
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%postun 100dpi-ISO8859-6
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%post ISO8859-7
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%postun ISO8859-7
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%post 75dpi-ISO8859-7
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%postun 75dpi-ISO8859-7
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%post 100dpi-ISO8859-7
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%postun 100dpi-ISO8859-7
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%post ISO8859-8
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%postun ISO8859-8
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%post 75dpi-ISO8859-8
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%postun 75dpi-ISO8859-8
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%post 100dpi-ISO8859-8
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%postun 100dpi-ISO8859-8
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%post ISO8859-9
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%postun ISO8859-9
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%post 75dpi-ISO8859-9
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%postun 75dpi-ISO8859-9
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%post 100dpi-ISO8859-9
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%postun 100dpi-ISO8859-9
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%post ISO8859-10
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%postun ISO8859-10
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%post 75dpi-ISO8859-10
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%postun 75dpi-ISO8859-10
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%post 100dpi-ISO8859-10
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%postun 100dpi-ISO8859-10
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%post ISO8859-11
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%postun ISO8859-11
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%post 75dpi-ISO8859-11
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%postun 75dpi-ISO8859-11
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%post 100dpi-ISO8859-11
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%postun 100dpi-ISO8859-11
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%post ISO8859-12
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%postun ISO8859-12
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%post 75dpi-ISO8859-12
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%postun 75dpi-ISO8859-12
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%post 100dpi-ISO8859-12
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%postun 100dpi-ISO8859-12
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%post ISO8859-13
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%postun ISO8859-13
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%post 75dpi-ISO8859-13
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%postun 75dpi-ISO8859-13
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%post 100dpi-ISO8859-13
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%postun 100dpi-ISO8859-13
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%post ISO8859-14
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%postun ISO8859-14
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%post 75dpi-ISO8859-14
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%postun 75dpi-ISO8859-14
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%post 100dpi-ISO8859-14
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%postun 100dpi-ISO8859-14
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%post ISO8859-15
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%postun ISO8859-15
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%post 75dpi-ISO8859-15
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%postun 75dpi-ISO8859-15
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%post 100dpi-ISO8859-15
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%postun 100dpi-ISO8859-15
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%post KOI8-R
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir
cd %{_fontsdir}/cyrillic
umask 022
%{_bindir}/mkfontdir

%postun KOI8-R
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir
cd %{_fontsdir}/cyrillic
umask 022
%{_bindir}/mkfontdir

%post 75dpi-KOI8-R
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%postun 75dpi-KOI8-R
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%post 100dpi-KOI8-R
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%postun 100dpi-KOI8-R
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%post JISX0201.1976-0
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%postun JISX0201.1976-0
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir

%post 75dpi-JISX0201.1976-0
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%postun 75dpi-JISX0201.1976-0
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%post 100dpi-JISX0201.1976-0
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%postun 100dpi-JISX0201.1976-0
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%files
%defattr(644,root,root,755)
%dir %{_fontsdir}/CID
%dir %{_fontsdir}/Speedo
%dir %{_fontsdir}/TTF
%dir %{_fontsdir}/encodings
%dir %{_fontsdir}/local
%{_fontsdir}/Speedo/*.spd
%{_fontsdir}/TTF/*.ttf
%{_fontsdir}/encodings/*
%{_t1fontsdir}/*[a-z_].pfb
%{_t1afmdir}/*[a-z_].afm
%{_t1fontsdir}/*.%{name}
%{_fontsdir}/TTF/fonts.scale.%{name}
%verify(not mtime size md5) %{_fontsdir}/CID/fonts.*
%verify(not mtime size md5) %{_fontsdir}/Speedo/fonts.*
%verify(not mtime size md5) %{_fontsdir}/TTF/fonts.dir
%verify(not mtime size md5) %{_fontsdir}/local/fonts.*
%verify(not mtime size md5) %{_fontsdir}/misc/fonts.dir
%verify(not mtime size md5) %{_fontsdir}/misc/fonts.alias.10XFree86-fonts
%{_fontsdir}/misc/10x20.pcf.gz
%{_fontsdir}/misc/12x24.pcf.gz
%{_fontsdir}/misc/5x7.pcf.gz
%{_fontsdir}/misc/5x8.pcf.gz
%{_fontsdir}/misc/6x10.pcf.gz
%{_fontsdir}/misc/6x12.pcf.gz
%{_fontsdir}/misc/6x13.pcf.gz
%{_fontsdir}/misc/6x13B.pcf.gz
%{_fontsdir}/misc/6x13O.pcf.gz
%{_fontsdir}/misc/6x9.pcf.gz
%{_fontsdir}/misc/7x13.pcf.gz
%{_fontsdir}/misc/7x13B.pcf.gz
%{_fontsdir}/misc/7x13O.pcf.gz
%{_fontsdir}/misc/7x14.pcf.gz
%{_fontsdir}/misc/7x14B.pcf.gz
%{_fontsdir}/misc/8x13.pcf.gz
%{_fontsdir}/misc/8x13B.pcf.gz
%{_fontsdir}/misc/8x13O.pcf.gz
%{_fontsdir}/misc/8x16.pcf.gz
%{_fontsdir}/misc/9x15.pcf.gz
%{_fontsdir}/misc/9x15B.pcf.gz
%{_fontsdir}/misc/9x18.pcf.gz
%{_fontsdir}/misc/9x18B.pcf.gz
%{_fontsdir}/misc/arabic*.pcf.gz
%{_fontsdir}/misc/c[^u]*.pcf.gz
%{_fontsdir}/misc/cu[^r]*.pcf.gz
%{_fontsdir}/misc/[d-e]*.pcf.gz
%{_fontsdir}/misc/[g-h]*.pcf.gz
%{_fontsdir}/misc/k*.pcf.gz
%{_fontsdir}/misc/[m-z]*.pcf.gz
%{_fontsdir}/misc/*rk.pcf.gz
%{_fontsdir}/misc/*ko.pcf.gz

%files base
%defattr(644,root,root,755)
%dir %{_fontsdir}/misc
%{_fontsdir}/misc/cursor.pcf.gz
%{_fontsdir}/misc/6x13-ISO8859-1.pcf.gz
%{_fontsdir}/misc/fonts.alias.00XFree86-fonts-base

%ifnarch alpha
%files PEX
%defattr(644,root,root,755)
%{_fontsdir}/PEX
%endif

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_fontsdir}/util

%files 75dpi
%defattr(644,root,root,755)
%dir %{_fontsdir}/75dpi
%{_fontsdir}/75dpi/*[a-zA-Z_][0-9][0-9].pcf.gz
%verify(not mtime size md5) %{_fontsdir}/75dpi/fonts.*
%verify(not mtime size md5) %{_fontsdir}/75dpi/encodings.dir

%files 100dpi
%defattr(644,root,root,755)
%dir %{_fontsdir}/100dpi
%{_fontsdir}/100dpi/*[a-zA-Z_][0-9][0-9].pcf.gz
%verify(not mtime size md5) %{_fontsdir}/100dpi/fonts.*
%verify(not mtime size md5) %{_fontsdir}/100dpi/encodings.dir

%files ISO8859-1
%defattr(644,root,root,755)
%{_fontsdir}/misc/[^6]*ISO8859-1.pcf.gz
%{_fontsdir}/misc/6x1[^3]*ISO8859-1.pcf.gz
%{_fontsdir}/misc/6x13[BO]-ISO8859-1.pcf.gz

%files 75dpi-ISO8859-1
%defattr(644,root,root,755)
%{_fontsdir}/75dpi/*ISO8859-1.pcf.gz

%files 100dpi-ISO8859-1
%defattr(644,root,root,755)
%{_fontsdir}/100dpi/*ISO8859-1.pcf.gz

%files ISO8859-2
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-2.pcf.gz

%files 75dpi-ISO8859-2
%defattr(644,root,root,755)
%{_fontsdir}/75dpi/*ISO8859-2.pcf.gz

%files 100dpi-ISO8859-2
%defattr(644,root,root,755)
%{_fontsdir}/100dpi/*ISO8859-2.pcf.gz

%files Type1-ISO8859-2
%defattr(644,root,root,755)
%{_t1fontsdir}/*-ISO-8859-2*
%{_t1afmdir}/*-ISO-8859-2*.afm
%{_t1pfmdir}/*-ISO-8859-2*.pfm
%{_t1fontsdir}/*.XFree86-fonts-Type1-ISO8859-2

%files ISO8859-3
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-3.pcf.gz

%files 75dpi-ISO8859-3
%defattr(644,root,root,755)
%{_fontsdir}/75dpi/*ISO8859-3.pcf.gz

%files 100dpi-ISO8859-3
%defattr(644,root,root,755)
%{_fontsdir}/100dpi/*ISO8859-3.pcf.gz

%files ISO8859-4
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-4.pcf.gz

%files 75dpi-ISO8859-4
%defattr(644,root,root,755)
%{_fontsdir}/75dpi/*ISO8859-4.pcf.gz

%files 100dpi-ISO8859-4
%defattr(644,root,root,755)
%{_fontsdir}/100dpi/*ISO8859-4.pcf.gz

%files ISO8859-5
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-5.pcf.gz

#%files 75dpi-ISO8859-5
#%defattr(644,root,root,755)
#%{_fontsdir}/75dpi/*ISO8859-5.pcf.gz

#%files 100dpi-ISO8859-5
#%defattr(644,root,root,755)
#%{_fontsdir}/100dpi/*ISO8859-5.pcf.gz

#%files ISO8859-6
#%defattr(644,root,root,755)
#%{_fontsdir}/misc/*ISO8859-6.pcf.gz

#%files 75dpi-ISO8859-6
#%defattr(644,root,root,755)
#%{_fontsdir}/75dpi/*ISO8859-6.pcf.gz

#%files 100dpi-ISO8859-6
#%defattr(644,root,root,755)
#%{_fontsdir}/100dpi/*ISO8859-6.pcf.gz

%files ISO8859-7
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-7.pcf.gz

#%files 75dpi-ISO8859-7
#%defattr(644,root,root,755)
#%{_fontsdir}/75dpi/*ISO8859-7.pcf.gz

#%files 100dpi-ISO8859-7
#%defattr(644,root,root,755)
#%{_fontsdir}/100dpi/*ISO8859-7.pcf.gz

%files ISO8859-8
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-8.pcf.gz

#%files 75dpi-ISO8859-8
#%defattr(644,root,root,755)
#%{_fontsdir}/75dpi/*ISO8859-8.pcf.gz

#%files 100dpi-ISO8859-8
#%defattr(644,root,root,755)
#%{_fontsdir}/100dpi/*ISO8859-8.pcf.gz

%files ISO8859-9
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-9.pcf.gz

%files 75dpi-ISO8859-9
%defattr(644,root,root,755)
%{_fontsdir}/75dpi/*ISO8859-9.pcf.gz

%files 100dpi-ISO8859-9
%defattr(644,root,root,755)
%{_fontsdir}/100dpi/*ISO8859-9.pcf.gz

%files ISO8859-10
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-10.pcf.gz

%files 75dpi-ISO8859-10
%defattr(644,root,root,755)
%{_fontsdir}/75dpi/*ISO8859-10.pcf.gz

%files 100dpi-ISO8859-10
%defattr(644,root,root,755)
%{_fontsdir}/100dpi/*ISO8859-10.pcf.gz

#%files ISO8859-11
#%defattr(644,root,root,755)
#%{_fontsdir}/misc/*ISO8859-11.pcf.gz

#%files 75dpi-ISO8859-11
#%defattr(644,root,root,755)
#%{_fontsdir}/75dpi/*ISO8859-11.pcf.gz

#%files 100dpi-ISO8859-11
#%defattr(644,root,root,755)
#%{_fontsdir}/100dpi/*ISO8859-11.pcf.gz

#%files ISO8859-12
#%defattr(644,root,root,755)
#%{_fontsdir}/misc/*ISO8859-12.pcf.gz

#%files 75dpi-ISO8859-12
#%defattr(644,root,root,755)
#%{_fontsdir}/75dpi/*ISO8859-12.pcf.gz

#%files 100dpi-ISO8859-12
#%defattr(644,root,root,755)
#%{_fontsdir}/100dpi/*ISO8859-12.pcf.gz

%files ISO8859-13
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-13.pcf.gz

%files 75dpi-ISO8859-13
%defattr(644,root,root,755)
%{_fontsdir}/75dpi/*ISO8859-13.pcf.gz

%files 100dpi-ISO8859-13
%defattr(644,root,root,755)
%{_fontsdir}/100dpi/*ISO8859-13.pcf.gz

%files ISO8859-14
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-14.pcf.gz

%files 75dpi-ISO8859-14
%defattr(644,root,root,755)
%{_fontsdir}/75dpi/*ISO8859-14.pcf.gz

%files 100dpi-ISO8859-14
%defattr(644,root,root,755)
%{_fontsdir}/100dpi/*ISO8859-14.pcf.gz

%files ISO8859-15
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-15.pcf.gz

%files 75dpi-ISO8859-15
%defattr(644,root,root,755)
%{_fontsdir}/75dpi/*ISO8859-15.pcf.gz

%files 100dpi-ISO8859-15
%defattr(644,root,root,755)
%{_fontsdir}/100dpi/*ISO8859-15.pcf.gz

%files KOI8-R
%defattr(644,root,root,755)
%{_fontsdir}/misc/*KOI8-R.pcf.gz
%{_fontsdir}/cyrillic

#%files 75dpi-KOI8-R
#%defattr(644,root,root,755)
#
#%files 100dpi-KOI8-R
#%defattr(644,root,root,755)

%files JISX0201.1976-0
%defattr(644,root,root,755)
%{_fontsdir}/misc/*JISX0201.1976-0.pcf.gz
%{_fontsdir}/misc/*ja.pcf.gz
%{_fontsdir}/misc/jiskan*.pcf.gz

#%files 75dpi-JISX0201.1976-0
#%defattr(644,root,root,755)
#
#%files 100dpi-JISX0201.1976-0
#%defattr(644,root,root,755)

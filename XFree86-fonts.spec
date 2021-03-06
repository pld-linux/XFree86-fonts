Summary:	XFree86 Fonts
Summary(pl.UTF-8):	Fonty dla systemu XFree86
Name:		XFree86-fonts
Version:	4.8.0
Release:	1
License:	MIT
Group:		Fonts
# We need source0 for arabic fonts
Source0:	http://ftp.xfree86.org/pub/XFree86/%{version}/source/XFree86-%{version}-src-1.tgz
# Source0-md5:	42d802caf03cbaadfa3a69b887e9b203
Source1:	http://ftp.xfree86.org/pub/XFree86/%{version}/source/XFree86-%{version}-src-4.tgz
# Source1-md5:	2743099973f1bd3a73bcb7b05df0f279
Source2:	http://ftp.xfree86.org/pub/XFree86/%{version}/source/XFree86-%{version}-src-5.tgz
# Source2-md5:	236c807d4f426850f24784ccceec08ab
Source3:	%{name}.Fontmap
Patch0:		%{name}-extras-fix.patch
Patch1:		%{name}-do_not_run_fccache.patch
Patch2:		%{name}-TTF_build.patch
# allow utils from X11R7
%if %(test -x /usr/bin/bdftopcf ; echo $?)
BuildRequires:	XFree86-devel
%else
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-util-imake
%endif
BuildRequires:	perl-base
BuildRequires:	t1utils
Requires(post,postun):	fontpostinst
Requires:	%{name}-base = %{version}
Requires:	%{_fontsdir}/misc
Requires:	%{_fontsdir}/Type1
Obsoletes:	XFree86-latin2-fonts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_t1fontsdir	%{_fontsdir}/Type1
%define		_t1afmdir	%{_t1fontsdir}/afm
%define		_t1pfmdir	%{_t1fontsdir}/pfm

%if %(test -d /usr/%{_lib}/X11/config ; echo $?)
%define		xconfdir	%{_prefix}/lib/X11/config
%else
%define		xconfdir	/usr/%{_lib}/X11/config
%endif

%description
This package contains some common used fonts. Normally fonts are
needed only by X server (either locally to server or through xfs).

%description -l pl.UTF-8
Pakiet ten zawiera często używane fonty. Zwykle fonty są potrzebne
tylko dla X serwera (lokalnie dla serwera lub poprzez xfs).

%package utils
Summary:	Perl scripts for generating BDF fonts
Summary(pl.UTF-8):	Skrypty perlowe do generowania fontów BDF
Group:		X11

%description utils
Perl scripts that allow to generate from an ISO10646-1 encoded BDF
font other BDF fonts in any possible encoding.

%description utils -l pl.UTF-8
Skrypty perlowe pozwalające wygenerować z fontów BDF kodowanych w
ISO10646-1 fonty BDF z dowolnym kodowaniem.

%package base
Summary:	Base fonts (cursor and fixed)
Summary(pl.UTF-8):	Podstawowe fonty (cursor i fixed)
Group:		Fonts
Requires(post,postun):	fontpostinst

%description base
Base fonts (cursor and fixed) needed to start X server.

%description base -l pl.UTF-8
Podstawowe fonty (cursor i fixed) niezbędne do uruchomienia X serwera.

%package ISO8859-1
Summary:	ISO-8859-1 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-1
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-1
ISO-8859-1 basic raster fonts.

%description ISO8859-1 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-1.

%package ISO8859-2
Summary:	ISO-8859-2 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-2
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-2
ISO-8859-2 basic raster fonts.

%description ISO8859-2 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-2.

%package ISO8859-3
Summary:	ISO-8859-3 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-3
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-3
ISO-8859-3 basic raster fonts.

%description ISO8859-3 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-3.

%package ISO8859-4
Summary:	ISO-8859-4 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-4
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-4
ISO-8859-4 basic raster fonts.

%description ISO8859-4 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-4.

%package ISO8859-5
Summary:	ISO-8859-5 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-5
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-5
Basic ISO-8859-5 raster fonts.

%description ISO8859-5 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-5.

%package ISO8859-6
Summary:	ISO-8859-6 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-6
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-6
ISO-8859-6 basic raster fonts.

%description ISO8859-6 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-6.

%package ISO8859-7
Summary:	ISO-8859-7 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-7
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-7
ISO-8859-7 basic raster fonts.

%description ISO8859-7 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-7.

%package ISO8859-8
Summary:	ISO-8859-8 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-8
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-8
ISO-8859-8 basic raster fonts.

%description ISO8859-8 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-8.

%package ISO8859-9
Summary:	ISO-8859-9 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-9
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-9
ISO-8859-9 basic raster fonts.

%description ISO8859-9 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-9.

%package ISO8859-10
Summary:	ISO-8859-10 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-10
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-10
ISO-8859-10 basic raster fonts.

%description ISO8859-10 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-10.

%package ISO8859-11
Summary:	ISO-8859-11 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-11
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-11
ISO-8859-11 basic raster fonts.

%description ISO8859-11 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-11.

%package ISO8859-12
Summary:	ISO-8859-12 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-12
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-12
ISO-8859-12 basic raster fonts.

%description ISO8859-12 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-12.

%package ISO8859-13
Summary:	ISO-8859-13 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-13
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-13
ISO-8859-13 basic raster fonts.

%description ISO8859-13 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-13.

%package ISO8859-14
Summary:	ISO-8859-14 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-14
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-14
ISO-8859-14 basic raster fonts.

%description ISO8859-14 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-14.

%package ISO8859-15
Summary:	ISO-8859-15 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-15
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-15
ISO-8859-15 basic raster fonts.

%description ISO8859-15 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-15.

%package ISO8859-16
Summary:	ISO-8859-16 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-16
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-16
ISO-8859-16 basic raster fonts.

%description ISO8859-16 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-16.

%package JISX0201.1976-0
Summary:	JISX0201.1976-0 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe JISX0201.1976-0
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description JISX0201.1976-0
JISX0201.1976-0 basic raster fonts.

%description JISX0201.1976-0 -l pl.UTF-8
Podstawowe fonty rastrowe JISX0201.1976-0.

%package KOI8-R
Summary:	KOI8-R (cyrillic) raster fonts
Summary(pl.UTF-8):	Fonty rastrowe KOI8-R (cyrylica)
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
Obsoletes:	XFree86-cyrillic-fonts

%description KOI8-R
KOI8-R (cyrillic) raster fonts.

%description KOI8-R -l pl.UTF-8
Fonty rastrowe KOI8-R (cyrylica).

%package 75dpi
Summary:	X11R6 75dpi raster fonts
Summary(de.UTF-8):	X11R6 75 dpi-Fonts
Summary(fr.UTF-8):	Fontes 75 dpi X11R6
Summary(pl.UTF-8):	Fonty rastrowe o rozdzielczości 75dpi
Summary(tr.UTF-8):	X11R6 75dpi yazıtipleri
Group:		Fonts
Requires(post,postun):	fontpostinst
Obsoletes:	XFree86-75dpi-fonts
%ifarch sparc
Obsoletes:	X11R6.1-75dpi-fonts
%endif

%description 75dpi
The 75dpi fonts used on most Linux systems. Users with high resolution
displays may prefer the 100dpi fonts available in a separate package.

%description 75dpi -l de.UTF-8
Die 75dpi-Fonts, die auf meisten Linux-Systemen verwendet werden. Für
Benutzer mit einer hochauflösender Darstellung sind die 100dpi-Fonts
eines getrennt erhältlichen Pakets besser geeignet.

%description 75dpi -l fr.UTF-8
Fontes 75 dpi utilisées sur la plupart des systèmes Linux. Ceux qui
ont des écrans à haute résolution préfèreront les fontes 100 dpi
disponibles dans un autre paquetage.

%description 75dpi -l pl.UTF-8
Pakiet ten zawiera fonty rastrowe 75dpi. W wypadku większej
rozdzielczości zalecane są fonty 100dpi, które są dostępne w osobnym
pakiecie.

%description 75dpi -l tr.UTF-8
Çoğu Linux sisteminde 75dpi yazıtipi kullanılır. Yüksek çözünürlük
kullanan kullanıcılar 100dpi yazıtiplerini yeğleyebilirler.

%package 75dpi-ISO8859-1
Summary:	ISO-8859-1 75dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-1 o rozdzielczości 75dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/75dpi

%description 75dpi-ISO8859-1
ISO-8859-1 75dpi raster fonts.

%description 75dpi-ISO8859-1 -l pl.UTF-8
Fonty rastrowe ISO-8859-1 o rozdzielczości 75dpi.

%package 75dpi-ISO8859-2
Summary:	ISO-8859-2 75dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-2 o rozdzielczości 75dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/75dpi
Obsoletes:	XFree86-ISO8859-2-75dpi-fonts
Obsoletes:	XFree86-latin2-75dpi-fonts

%description 75dpi-ISO8859-2
ISO-8859-2 75dpi raster fonts.

%description 75dpi-ISO8859-2 -l pl.UTF-8
Fonty rastrowe ISO-8859-2 o rozdzielczości 75dpi.

%package 75dpi-ISO8859-3
Summary:	ISO-8859-3 75dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-3 o rozdzielczości 75dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/75dpi

%description 75dpi-ISO8859-3
ISO-8859-3 75dpi raster fonts.

%description 75dpi-ISO8859-3 -l pl.UTF-8
Fonty rastrowe ISO-8859-3 o rozdzielczości 75dpi.

%package 75dpi-ISO8859-4
Summary:	ISO-8859-4 75dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-4 o rozdzielczości 75dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/75dpi

%description 75dpi-ISO8859-4
ISO-8859-4 75dpi raster fonts.

%description 75dpi-ISO8859-4 -l pl.UTF-8
Fonty rastrowe ISO-8859-4 o rozdzielczości 75dpi.

%package 75dpi-ISO8859-5
Summary:	ISO-8859-5 75dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-5 o rozdzielczości 75dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/75dpi

%description 75dpi-ISO8859-5
ISO-8859-5 75dpi raster fonts.

%description 75dpi-ISO8859-5 -l pl.UTF-8
Fonty rastrowe ISO-8859-5 o rozdzielczości 75dpi.

%package 75dpi-ISO8859-6
Summary:	ISO-8859-6 75dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-6 o rozdzielczości 75dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/75dpi

%description 75dpi-ISO8859-6
ISO-8859-6 75dpi raster fonts.

%description 75dpi-ISO8859-6 -l pl.UTF-8
Fonty rastrowe ISO-8859-6 o rozdzielczości 75dpi.

%package 75dpi-ISO8859-7
Summary:	ISO-8859-7 75dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-7 o rozdzielczości 75dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/75dpi

%description 75dpi-ISO8859-7
ISO-8859-7 75dpi raster fonts.

%description 75dpi-ISO8859-7 -l pl.UTF-8
Fonty rastrowe ISO-8859-7 o rozdzielczości 75dpi.

%package 75dpi-ISO8859-8
Summary:	ISO-8859-8 75dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-8 o rozdzielczości 75dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/75dpi

%description 75dpi-ISO8859-8
ISO-8859-8 75dpi raster fonts.

%description 75dpi-ISO8859-8 -l pl.UTF-8
Fonty rastrowe ISO-8859-8 o rozdzielczości 75dpi.

%package 75dpi-ISO8859-9
Summary:	ISO-8859-9 75dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-9 o rozdzielczości 75dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/75dpi

%description 75dpi-ISO8859-9
ISO-8859-9 75dpi raster fonts.

%description 75dpi-ISO8859-9 -l pl.UTF-8
Fonty rastrowe ISO-8859-9 o rozdzielczości 75dpi.

%package 75dpi-ISO8859-10
Summary:	ISO-8859-10 75dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-10 o rozdzielczości 75dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/75dpi

%description 75dpi-ISO8859-10
ISO-8859-10 75dpi raster fonts.

%description 75dpi-ISO8859-10 -l pl.UTF-8
Fonty rastrowe ISO-8859-10 o rozdzielczości 75dpi.

%package 75dpi-ISO8859-11
Summary:	ISO-8859-11 75dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-11 o rozdzielczości 75dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/75dpi

%description 75dpi-ISO8859-11
ISO-8859-11 75dpi raster fonts.

%description 75dpi-ISO8859-11 -l pl.UTF-8
Fonty rastrowe ISO-8859-11 o rozdzielczości 75dpi.

%package 75dpi-ISO8859-12
Summary:	ISO-8859-12 75dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-12 o rozdzielczości 75dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/75dpi

%description 75dpi-ISO8859-12
ISO-8859-12 75dpi raster fonts.

%description 75dpi-ISO8859-12 -l pl.UTF-8
Fonty rastrowe ISO-8859-12 o rozdzielczości 75dpi.

%package 75dpi-ISO8859-13
Summary:	ISO-8859-13 75dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-13 o rozdzielczości 75dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/75dpi

%description 75dpi-ISO8859-13
ISO-8859-13 75dpi raster fonts.

%description 75dpi-ISO8859-13 -l pl.UTF-8
Fonty rastrowe ISO-8859-13 o rozdzielczości 75dpi.

%package 75dpi-ISO8859-14
Summary:	ISO-8859-14 75dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-14 o rozdzielczości 75dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/75dpi

%description 75dpi-ISO8859-14
ISO-8859-14 75dpi raster fonts.

%description 75dpi-ISO8859-14 -l pl.UTF-8
Fonty rastrowe ISO-8859-14 o rozdzielczości 75dpi.

%package 75dpi-ISO8859-15
Summary:	ISO-8859-15 75dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-15 o rozdzielczości 75dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/75dpi

%description 75dpi-ISO8859-15
ISO-8859-15 75dpi raster fonts.

%description 75dpi-ISO8859-15 -l pl.UTF-8
Fonty rastrowe ISO-8859-15 o rozdzielczości 75dpi.

%package 75dpi-JISX0201.1976-0
Summary:	JISX0201.1976-0 75dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe JISX0201.1976-0 o rozdzielczości 75dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/75dpi

%description 75dpi-JISX0201.1976-0
JISX0201.1976-0 75dpi raster fonts.

%description 75dpi-JISX0201.1976-0 -l pl.UTF-8
Fonty rastrowe JISX0201.1976-0 o rozdzielczości 75dpi.

%package 75dpi-KOI8-R
Summary:	KOI8-R 75dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe KOI8-R o rozdzielczości 75dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/75dpi

%description 75dpi-KOI8-R
KOI8-R 75dpi raster fonts.

%description 75dpi-KOI8-R -l pl.UTF-8
Fonty rastrowe ISO-KOI8-R o rozdzielczości 75dpi.

%package 100dpi
Summary:	X11R6 100dpi raster fonts
Summary(de.UTF-8):	X11R6 100dpi-Fonts
Summary(fr.UTF-8):	Fontes 100ppp pour X11R6
Summary(pl.UTF-8):	Fonty rastrowe o rozdzielczości 100dpi
Summary(tr.UTF-8):	X11R6 100dpi yazıtipleri
Group:		Fonts
Requires(post,postun):	fontpostinst
Obsoletes:	XFree86-100dpi-fonts
%ifarch sparc
Obsoletes:	X11R6.1-100dpi-fonts
%endif

%description 100dpi
The 100dpi fonts used on most Linux systems. Users with low resolution
displays may prefer the 75dpi fonts available in a separate package.

%description 100dpi -l de.UTF-8
Die 100dpi-Schriftarten, die auf den meisten Linux-Systemen zum
Einsatz kommen. Anwender mit hochauflösenden Monitoren ziehen unter
Umständen die 100dpi-Schriften vor, die in einem separaten Paket
erhältlich sind.

%description 100dpi -l fr.UTF-8
Les fontes 100dpi sont utilisées par la plupart des systèmes Linux.
Les utilisateurs ayant des hautes résolutions peuvent préférer les
fontes 100dpi disponibles dans un package séparé.

%description 100dpi -l pl.UTF-8
Pakiet ten zawiera fonty rastrowe 100dpi. Bedą one potrzebne przy
pracy w dużych rozdzielczościach.

%description 100dpi -l tr.UTF-8
Yüksek çözünürlük kullanan kullanıcılar 100dpi yazıtiplerini 75dpi
olanlara yeğleyebilirler.

%package 100dpi-ISO8859-1
Summary:	ISO-8859-1 100dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-1 o rozdzielczości 100dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi

%description 100dpi-ISO8859-1
ISO-8859-1 100dpi raster fonts.

%description 100dpi-ISO8859-1 -l pl.UTF-8
Fonty rastrowe ISO-8859-1 o rozdzielczości 100dpi.

%package 100dpi-ISO8859-2
Summary:	ISO-8859-2 100dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-2 o rozdzielczości 100dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi
Obsoletes:	XFree86-ISO8859-2-100dpi-fonts
Obsoletes:	XFree86-latin2-100dpi-fonts

%description 100dpi-ISO8859-2
ISO-8859-2 100dpi raster fonts.

%description 100dpi-ISO8859-2 -l pl.UTF-8
Fonty rastrowe ISO-8859-2 o rozdzielczości 100dpi.

%package 100dpi-ISO8859-3
Summary:	ISO-8859-3 100dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-3 o rozdzielczości 100dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi

%description 100dpi-ISO8859-3
ISO-8859-3 100dpi raster fonts.

%description 100dpi-ISO8859-3 -l pl.UTF-8
Fonty rastrowe ISO-8859-3 o rozdzielczości 100dpi.

%package 100dpi-ISO8859-4
Summary:	ISO-8859-4 100dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-4 o rozdzielczości 100dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi

%description 100dpi-ISO8859-4
ISO-8859-4 100dpi raster fonts.

%description 100dpi-ISO8859-4 -l pl.UTF-8
Fonty rastrowe ISO-8859-4 o rozdzielczości 100dpi.

%package 100dpi-ISO8859-5
Summary:	ISO-8859-5 100dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-5 o rozdzielczości 100dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi

%description 100dpi-ISO8859-5
ISO-8859-5 100dpi raster fonts.

%description 100dpi-ISO8859-5 -l pl.UTF-8
Fonty rastrowe ISO-8859-5 o rozdzielczości 100dpi.

%package 100dpi-ISO8859-6
Summary:	ISO-8859-6 100dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-6 o rozdzielczości 100dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi

%description 100dpi-ISO8859-6
ISO-8859-6 100dpi raster fonts.

%description 100dpi-ISO8859-6 -l pl.UTF-8
Fonty rastrowe ISO-8859-6 o rozdzielczości 100dpi.

%package 100dpi-ISO8859-7
Summary:	ISO-8859-7 100dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-7 o rozdzielczości 100dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi

%description 100dpi-ISO8859-7
ISO-8859-7 100dpi raster fonts.

%description 100dpi-ISO8859-7 -l pl.UTF-8
Fonty rastrowe ISO-8859-7 o rozdzielczości 100dpi.

%package 100dpi-ISO8859-8
Summary:	ISO-8859-8 100dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-8 o rozdzielczości 100dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi

%description 100dpi-ISO8859-8
ISO-8859-8 100dpi raster fonts.

%description 100dpi-ISO8859-8 -l pl.UTF-8
Fonty rastrowe ISO-8859-8 o rozdzielczości 100dpi.

%package 100dpi-ISO8859-9
Summary:	ISO-8859-9 100dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-9 o rozdzielczości 100dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi

%description 100dpi-ISO8859-9
ISO-8859-9 100dpi raster fonts.

%description 100dpi-ISO8859-9 -l pl.UTF-8
Fonty rastrowe ISO-8859-9 o rozdzielczości 100dpi.

%package 100dpi-ISO8859-10
Summary:	ISO-8859-10 100dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-10 o rozdzielczości 100dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi

%description 100dpi-ISO8859-10
ISO-8859-10 100dpi raster fonts.

%description 100dpi-ISO8859-10 -l pl.UTF-8
Fonty rastrowe ISO-8859-10 o rozdzielczości 100dpi.

%package 100dpi-ISO8859-11
Summary:	ISO-8859-11 100dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-11 o rozdzielczości 100dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi

%description 100dpi-ISO8859-11
ISO-8859-11 100dpi raster fonts.

%description 100dpi-ISO8859-11 -l pl.UTF-8
Fonty rastrowe ISO-8859-11 o rozdzielczości 100dpi.

%package 100dpi-ISO8859-12
Summary:	ISO-8859-12 100dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-12 o rozdzielczości 100dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi

%description 100dpi-ISO8859-12
ISO-8859-12 100dpi raster fonts.

%description 100dpi-ISO8859-12 -l pl.UTF-8
Fonty rastrowe ISO-8859-12 o rozdzielczości 100dpi.

%package 100dpi-ISO8859-13
Summary:	ISO-8859-13 100dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-13 o rozdzielczości 100dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi

%description 100dpi-ISO8859-13
ISO-8859-13 100dpi raster fonts.

%description 100dpi-ISO8859-13 -l pl.UTF-8
Fonty rastrowe ISO-8859-13 o rozdzielczości 100dpi.

%package 100dpi-ISO8859-14
Summary:	ISO-8859-14 100dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-14 o rozdzielczości 100dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi

%description 100dpi-ISO8859-14
ISO-8859-14 100dpi raster fonts.

%description 100dpi-ISO8859-14 -l pl.UTF-8
Fonty rastrowe ISO-8859-14 o rozdzielczości 100dpi.

%package 100dpi-ISO8859-15
Summary:	ISO-8859-15 100dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe ISO-8859-15 o rozdzielczości 100dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi

%description 100dpi-ISO8859-15
ISO-8859-15 100dpi raster fonts.

%description 100dpi-ISO8859-15 -l pl.UTF-8
Fonty rastrowe ISO-8859-15 o rozdzielczości 100dpi.

%package 100dpi-JISX0201.1976-0
Summary:	JISX0201.1976-0 100dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe JISX0201.1976-0 o rozdzielczości 100dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi

%description 100dpi-JISX0201.1976-0
JISX0201.1976-0 100dpi raster fonts.

%description 100dpi-JISX0201.1976-0 -l pl.UTF-8
Fonty rastrowe JISX0201.1976-0 o rozdzielczości 100dpi.

%package 100dpi-KOI8-R
Summary:	KOI8-R 100dpi raster fonts
Summary(pl.UTF-8):	Fonty rastrowe KOI8-R o rozdzielczości 100dpi
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi

%description 100dpi-KOI8-R
KOI8-R 100dpi raster fonts.

%description 100dpi-KOI8-R -l pl.UTF-8
Fonty rastrowe KOI8-R o rozdzielczości 100dpi.

%package Ethiopic
Summary:	Ethiopic OpenType and TrueType fonts
Summary(pl.UTF-8):	Etiopskie fonty OpenType i TrueType
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/OTF
Requires:	%{_fontsdir}/TTF

%description Ethiopic
Ethiopic OpenType and TrueType fonts.

%description Ethiopic -l pl.UTF-8
Etiopskie fonty OpenType i TrueType.

%package Syriac
Summary:	Syriac OpenType fonts
Summary(pl.UTF-8):	Starosyryjskie fonty OpenType
License:	distributable without modifications
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/OTF

%description Syriac
Syriac OpenType fonts.

%description Syriac -l pl.UTF-8
Starosyryjskie fonty OpenType.

%prep
%setup -qc -a1 -a2
%patch0 -p0
%patch1 -p0
%patch2 -p1

cp -f xc/extras/fonts/arabic24/*.bdf xc/fonts/bdf/misc
cp -f xc/extras/fonts/ClearlyU/*.bdf xc/fonts/bdf/misc

%build
cd xc/fonts
imake -DBuildFonts -DUseInstalled -I%{xconfdir}
%{__make} Makefiles
cd scaled
imake -DBuildFonts -DBuildEthiopicFonts -DBuildBethMarduthoFonts -DBuildSpeedoFonts \
	-DUseInstalled -I%{xconfdir}
%{__make} Makefiles
cd ..
%{__make} depend
cd ..
%{__make} -C fonts \
	TOP=`pwd` \
	UCS2ANY=`pwd`/fonts/util/ucs2any.pl \
	BDFTRUNCATE=`pwd`/fonts/util/bdftruncate.pl \
	UCSMAPPREFIX=`pwd`/fonts/util/map- \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_t1afmdir}

cd xc
%{__make} -C fonts install \
	TOP=`pwd` \
	UCS2ANY=`pwd`/fonts/util/ucs2any.pl \
	BDFTRUNCATE=`pwd`/fonts/util/bdftruncate.pl \
	UCSMAPPREFIX=`pwd`/fonts/util/map- \
	BINDIR=%{_bindir} \
	FONTDIR=%{_fontsdir} \
	ENCODINGSDIR=%{_fontsdir}/encodings \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} -C fonts install.man \
	TOP=`pwd` \
	UCS2ANY=`pwd`/fonts/util/ucs2any.pl \
	BDFTRUNCATE=`pwd`/fonts/util/bdftruncate.pl \
	UCSMAPPREFIX=`pwd`/fonts/util/map- \
	MANDIR=%{_mandir}/man1 \
	DESTDIR=$RPM_BUILD_ROOT
cd ..

# separate *.afm, convert *.pfa to .pfb
mv -f $RPM_BUILD_ROOT%{_t1fontsdir}/*.afm $RPM_BUILD_ROOT%{_t1afmdir}
cd $RPM_BUILD_ROOT%{_t1fontsdir}
for f in *.pfa ; do
	t1binary $f `basename $f .pfa`.pfb
	rm -f $f
done
cd -

# split fonts.alias (separate "fixed")
grep -v '^fixed[ \t]' $RPM_BUILD_ROOT%{_fontsdir}/misc/fonts.alias \
	> $RPM_BUILD_ROOT%{_fontsdir}/misc/fonts.alias.10XFree86-fonts
grep '^fixed[ \t].*' $RPM_BUILD_ROOT%{_fontsdir}/misc/fonts.alias \
	> $RPM_BUILD_ROOT%{_fontsdir}/misc/fonts.alias.00XFree86-fonts-base
rm -f $RPM_BUILD_ROOT%{_fontsdir}/misc/fonts.alias

# support merging font aliases from other packages
mv -f $RPM_BUILD_ROOT%{_fontsdir}/cyrillic/fonts.alias{,.%{name}-KOI8-R}
mv -f $RPM_BUILD_ROOT%{_fontsdir}/75dpi/fonts.alias{,.%{name}-75dpi-ISO8859-1}
mv -f $RPM_BUILD_ROOT%{_fontsdir}/100dpi/fonts.alias{,.%{name}-100dpi-ISO8859-1}

# mkfontscale is not able to generate proper fonts.scale for these Type1 fonts
tail -n +2 xc/fonts/scaled/Type1/fonts.scale | sed -e 's/\.pfa/\.pfb/' \
	> $RPM_BUILD_ROOT%{_t1fontsdir}/fonts.scale.%{name}
rm -f $RPM_BUILD_ROOT%{_t1fontsdir}/fonts.scale
# Fontmap for Type1 fonts (generated by type1inst)
install %{SOURCE3} $RPM_BUILD_ROOT%{_t1fontsdir}/Fontmap.%{name}

# mkfontscale doesn't support Speedo fonts
tail -n +2 $RPM_BUILD_ROOT%{_fontsdir}/Speedo/fonts.scale \
	> $RPM_BUILD_ROOT%{_fontsdir}/Speedo/fonts.scale.XFree86-fonts
rm -f $RPM_BUILD_ROOT%{_fontsdir}/Speedo/fonts.scale

# does mkfontscale support CID fonts? it's safer to assume that doesn't
#tail -n +2 $RPM_BUILD_ROOT%{_fontsdir}/CID/fonts.scale \
#	> $RPM_BUILD_ROOT%{_fontsdir}/CID/fonts.scale.XFree86-fonts
#rm -f $RPM_BUILD_ROOT%{_fontsdir}/CID/fonts.scale

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc
#fontpostinst CID
fontpostinst Speedo
fontpostinst TTF
fontpostinst Type1
fontpostinst local

%postun
fontpostinst misc
#fontpostinst CID
fontpostinst Speedo
fontpostinst TTF
fontpostinst Type1
fontpostinst local

%post base
fontpostinst misc

%postun base
fontpostinst misc

%triggerpostun base -- XFree86-fonts < 4.2.0-6
fontpostinst misc

%post ISO8859-1
fontpostinst misc

%postun ISO8859-1
fontpostinst misc

%post ISO8859-2
fontpostinst misc

%postun ISO8859-2
fontpostinst misc

%post ISO8859-3
fontpostinst misc

%postun ISO8859-3
fontpostinst misc

%post ISO8859-4
fontpostinst misc

%postun ISO8859-4
fontpostinst misc

%post ISO8859-5
fontpostinst misc

%postun ISO8859-5
fontpostinst misc

%post ISO8859-6
fontpostinst misc

%postun ISO8859-6
fontpostinst misc

%post ISO8859-7
fontpostinst misc

%postun ISO8859-7
fontpostinst misc

%post ISO8859-8
fontpostinst misc

%postun ISO8859-8
fontpostinst misc

%post ISO8859-9
fontpostinst misc

%postun ISO8859-9
fontpostinst misc

%post ISO8859-10
fontpostinst misc

%postun ISO8859-10
fontpostinst misc

%post ISO8859-11
fontpostinst misc

%postun ISO8859-11
fontpostinst misc

%post ISO8859-12
fontpostinst misc

%postun ISO8859-12
fontpostinst misc

%post ISO8859-13
fontpostinst misc

%postun ISO8859-13
fontpostinst misc

%post ISO8859-14
fontpostinst misc

%postun ISO8859-14
fontpostinst misc

%post ISO8859-15
fontpostinst misc

%postun ISO8859-15
fontpostinst misc

%post ISO8859-16
fontpostinst misc

%postun ISO8859-16
fontpostinst misc

%post JISX0201.1976-0
fontpostinst misc

%postun JISX0201.1976-0
fontpostinst misc

%post KOI8-R
fontpostinst misc
fontpostinst cyrillic

%postun KOI8-R
fontpostinst misc
fontpostinst cyrillic

%post 75dpi
fontpostinst 75dpi

%postun 75dpi
fontpostinst 75dpi

%post 75dpi-ISO8859-1
fontpostinst 75dpi

%postun 75dpi-ISO8859-1
fontpostinst 75dpi

%post 75dpi-ISO8859-2
fontpostinst 75dpi

%postun 75dpi-ISO8859-2
fontpostinst 75dpi

%post 75dpi-ISO8859-3
fontpostinst 75dpi

%postun 75dpi-ISO8859-3
fontpostinst 75dpi

%post 75dpi-ISO8859-4
fontpostinst 75dpi

%postun 75dpi-ISO8859-4
fontpostinst 75dpi

%post 75dpi-ISO8859-5
fontpostinst 75dpi

%postun 75dpi-ISO8859-5
fontpostinst 75dpi

%post 75dpi-ISO8859-6
fontpostinst 75dpi

%postun 75dpi-ISO8859-6
fontpostinst 75dpi

%post 75dpi-ISO8859-7
fontpostinst 75dpi

%postun 75dpi-ISO8859-7
fontpostinst 75dpi

%post 75dpi-ISO8859-8
fontpostinst 75dpi

%postun 75dpi-ISO8859-8
fontpostinst 75dpi

%post 75dpi-ISO8859-9
fontpostinst 75dpi

%postun 75dpi-ISO8859-9
fontpostinst 75dpi

%post 75dpi-ISO8859-10
fontpostinst 75dpi

%postun 75dpi-ISO8859-10
fontpostinst 75dpi

%post 75dpi-ISO8859-11
fontpostinst 75dpi

%postun 75dpi-ISO8859-11
fontpostinst 75dpi

%post 75dpi-ISO8859-12
fontpostinst 75dpi

%postun 75dpi-ISO8859-12
fontpostinst 75dpi

%post 75dpi-ISO8859-13
fontpostinst 75dpi

%postun 75dpi-ISO8859-13
fontpostinst 75dpi

%post 75dpi-ISO8859-14
fontpostinst 75dpi

%postun 75dpi-ISO8859-14
fontpostinst 75dpi

%post 75dpi-ISO8859-15
fontpostinst 75dpi

%postun 75dpi-ISO8859-15
fontpostinst 75dpi

%post 75dpi-JISX0201.1976-0
fontpostinst 75dpi

%postun 75dpi-JISX0201.1976-0
fontpostinst 75dpi

%post 75dpi-KOI8-R
fontpostinst 75dpi

%postun 75dpi-KOI8-R
fontpostinst 75dpi

%post 100dpi
fontpostinst 100dpi

%postun 100dpi
fontpostinst 100dpi

%post 100dpi-ISO8859-1
fontpostinst 100dpi

%postun 100dpi-ISO8859-1
fontpostinst 100dpi

%post 100dpi-ISO8859-2
fontpostinst 100dpi

%postun 100dpi-ISO8859-2
fontpostinst 100dpi

%post 100dpi-ISO8859-3
fontpostinst 100dpi

%postun 100dpi-ISO8859-3
fontpostinst 100dpi

%post 100dpi-ISO8859-4
fontpostinst 100dpi

%postun 100dpi-ISO8859-4
fontpostinst 100dpi

%post 100dpi-ISO8859-5
fontpostinst 100dpi

%postun 100dpi-ISO8859-5
fontpostinst 100dpi

%post 100dpi-ISO8859-6
fontpostinst 100dpi

%postun 100dpi-ISO8859-6
fontpostinst 100dpi

%post 100dpi-ISO8859-7
fontpostinst 100dpi

%postun 100dpi-ISO8859-7
fontpostinst 100dpi

%post 100dpi-ISO8859-8
fontpostinst 100dpi

%postun 100dpi-ISO8859-8
fontpostinst 100dpi

%post 100dpi-ISO8859-9
fontpostinst 100dpi

%postun 100dpi-ISO8859-9
fontpostinst 100dpi

%post 100dpi-ISO8859-10
fontpostinst 100dpi

%postun 100dpi-ISO8859-10
fontpostinst 100dpi

%post 100dpi-ISO8859-11
fontpostinst 100dpi

%postun 100dpi-ISO8859-11
fontpostinst 100dpi

%post 100dpi-ISO8859-12
fontpostinst 100dpi

%postun 100dpi-ISO8859-12
fontpostinst 100dpi

%post 100dpi-ISO8859-13
fontpostinst 100dpi

%postun 100dpi-ISO8859-13
fontpostinst 100dpi

%post 100dpi-ISO8859-14
fontpostinst 100dpi

%postun 100dpi-ISO8859-14
fontpostinst 100dpi

%post 100dpi-ISO8859-15
fontpostinst 100dpi

%postun 100dpi-ISO8859-15
fontpostinst 100dpi

%post 100dpi-JISX0201.1976-0
fontpostinst 100dpi

%postun 100dpi-JISX0201.1976-0
fontpostinst 100dpi

%post 100dpi-KOI8-R
fontpostinst 100dpi

%postun 100dpi-KOI8-R
fontpostinst 100dpi

%post Ethiopic
fontpostinst OTF
fontpostinst TTF

%postun Ethiopic
fontpostinst OTF
fontpostinst TTF

%post Syriac
fontpostinst OTF

%postun Syriac
fontpostinst OTF

%files
%defattr(644,root,root,755)
%{_fontsdir}/encodings

%{_fontsdir}/misc/*.pcf.gz
%exclude %{_fontsdir}/misc/*-ISO8859-*.pcf.gz
%exclude %{_fontsdir}/misc/*-JISX0201.1976-0.pcf.gz
%exclude %{_fontsdir}/misc/*-KOI8-R.pcf.gz
%exclude %{_fontsdir}/misc/cursor.pcf.gz
%exclude %{_fontsdir}/misc/*ja.pcf.gz
%exclude %{_fontsdir}/misc/jiskan*.pcf.gz
%{_fontsdir}/misc/fonts.alias.10XFree86-fonts

##%dir %{_fontsdir}/CID
##%{_fontsdir}/CID/fonts.scale.%{name}
##%ghost %{_fontsdir}/CID/fonts.dir

%dir %{_fontsdir}/OTF

%dir %{_fontsdir}/Speedo
%{_fontsdir}/Speedo/*.spd
%{_fontsdir}/Speedo/fonts.scale.%{name}
%ghost %{_fontsdir}/Speedo/fonts.dir

%{_fontsdir}/TTF/luxi*.ttf
%ghost %{_fontsdir}/TTF/fonts.dir

# These fonts are in fonts-ttf-bitstream-vera package
##%{_fontsdir}/TTF/Vera*.ttf

%{_t1fontsdir}/*[a-z_].pfb
%{_t1fontsdir}/*.%{name}
%{_t1afmdir}/*[a-z_].afm

%dir %{_fontsdir}/local
%ghost %{_fontsdir}/local/fonts.dir

%files base
%defattr(644,root,root,755)
%{_fontsdir}/misc/cursor.pcf.gz
%{_fontsdir}/misc/6x13-ISO8859-1.pcf.gz
%{_fontsdir}/misc/fonts.alias.00XFree86-fonts-base
%ghost %{_fontsdir}/misc/fonts.dir

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_fontsdir}/util
%{_mandir}/man1/*

%files ISO8859-1
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-1.pcf.gz
%exclude %{_fontsdir}/misc/6x13-ISO8859-1.pcf.gz

%files ISO8859-2
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-2.pcf.gz

%files ISO8859-3
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-3.pcf.gz

%files ISO8859-4
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-4.pcf.gz

%files ISO8859-5
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-5.pcf.gz

#%files ISO8859-6
#%defattr(644,root,root,755)
#%%{_fontsdir}/misc/*ISO8859-6.pcf.gz

%files ISO8859-7
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-7.pcf.gz

%files ISO8859-8
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-8.pcf.gz

%files ISO8859-9
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-9.pcf.gz

%files ISO8859-10
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-10.pcf.gz

%files ISO8859-11
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-11.pcf.gz

#%files ISO8859-12
#%defattr(644,root,root,755)
#%%{_fontsdir}/misc/*ISO8859-12.pcf.gz

%files ISO8859-13
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-13.pcf.gz

%files ISO8859-14
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-14.pcf.gz

%files ISO8859-15
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-15.pcf.gz

%files ISO8859-16
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-16.pcf.gz

%files JISX0201.1976-0
%defattr(644,root,root,755)
%{_fontsdir}/misc/*JISX0201.1976-0.pcf.gz
%{_fontsdir}/misc/*ja.pcf.gz
%{_fontsdir}/misc/jiskan*.pcf.gz

%files KOI8-R
%defattr(644,root,root,755)
%{_fontsdir}/misc/*KOI8-R.pcf.gz
%dir %{_fontsdir}/cyrillic
%{_fontsdir}/cyrillic/*.pcf.gz
%{_fontsdir}/cyrillic/fonts.alias.%{name}-KOI8-R
%ghost %{_fontsdir}/cyrillic/fonts.dir

%files 75dpi
%defattr(644,root,root,755)
%dir %{_fontsdir}/75dpi
%{_fontsdir}/75dpi/*[a-zA-Z_][0-9][0-9].pcf.gz
%ghost %{_fontsdir}/75dpi/fonts.dir

%files 75dpi-ISO8859-1
%defattr(644,root,root,755)
%{_fontsdir}/75dpi/*ISO8859-1.pcf.gz
%{_fontsdir}/75dpi/fonts.alias.%{name}-75dpi-ISO8859-1

%files 75dpi-ISO8859-2
%defattr(644,root,root,755)
%{_fontsdir}/75dpi/*ISO8859-2.pcf.gz

%files 75dpi-ISO8859-3
%defattr(644,root,root,755)
%{_fontsdir}/75dpi/*ISO8859-3.pcf.gz

%files 75dpi-ISO8859-4
%defattr(644,root,root,755)
%{_fontsdir}/75dpi/*ISO8859-4.pcf.gz

#%files 75dpi-ISO8859-5
#%defattr(644,root,root,755)
#%%{_fontsdir}/75dpi/*ISO8859-5.pcf.gz

#%files 75dpi-ISO8859-6
#%defattr(644,root,root,755)
#%%{_fontsdir}/75dpi/*ISO8859-6.pcf.gz

#%files 75dpi-ISO8859-7
#%defattr(644,root,root,755)
#%%{_fontsdir}/75dpi/*ISO8859-7.pcf.gz

#%files 75dpi-ISO8859-8
#%defattr(644,root,root,755)
#%%{_fontsdir}/75dpi/*ISO8859-8.pcf.gz

%files 75dpi-ISO8859-9
%defattr(644,root,root,755)
%{_fontsdir}/75dpi/*ISO8859-9.pcf.gz

%files 75dpi-ISO8859-10
%defattr(644,root,root,755)
%{_fontsdir}/75dpi/*ISO8859-10.pcf.gz

#%files 75dpi-ISO8859-11
#%defattr(644,root,root,755)
#%%{_fontsdir}/75dpi/*ISO8859-11.pcf.gz

#%files 75dpi-ISO8859-12
#%defattr(644,root,root,755)
#%%{_fontsdir}/75dpi/*ISO8859-12.pcf.gz

%files 75dpi-ISO8859-13
%defattr(644,root,root,755)
%{_fontsdir}/75dpi/*ISO8859-13.pcf.gz

%files 75dpi-ISO8859-14
%defattr(644,root,root,755)
%{_fontsdir}/75dpi/*ISO8859-14.pcf.gz

%files 75dpi-ISO8859-15
%defattr(644,root,root,755)
%{_fontsdir}/75dpi/*ISO8859-15.pcf.gz

#%files 75dpi-JISX0201.1976-0
#%defattr(644,root,root,755)

#%files 75dpi-KOI8-R
#%defattr(644,root,root,755)

%files 100dpi
%defattr(644,root,root,755)
%dir %{_fontsdir}/100dpi
%{_fontsdir}/100dpi/*[a-zA-Z_][0-9][0-9].pcf.gz
%ghost %{_fontsdir}/100dpi/fonts.dir

%files 100dpi-ISO8859-1
%defattr(644,root,root,755)
%{_fontsdir}/100dpi/*ISO8859-1.pcf.gz
%{_fontsdir}/100dpi/fonts.alias.%{name}-100dpi-ISO8859-1

%files 100dpi-ISO8859-2
%defattr(644,root,root,755)
%{_fontsdir}/100dpi/*ISO8859-2.pcf.gz

%files 100dpi-ISO8859-3
%defattr(644,root,root,755)
%{_fontsdir}/100dpi/*ISO8859-3.pcf.gz

%files 100dpi-ISO8859-4
%defattr(644,root,root,755)
%{_fontsdir}/100dpi/*ISO8859-4.pcf.gz

#%files 100dpi-ISO8859-5
#%defattr(644,root,root,755)
#%%{_fontsdir}/100dpi/*ISO8859-5.pcf.gz

#%files 100dpi-ISO8859-6
#%defattr(644,root,root,755)
#%%{_fontsdir}/100dpi/*ISO8859-6.pcf.gz

#%files 100dpi-ISO8859-7
#%defattr(644,root,root,755)
#%%{_fontsdir}/100dpi/*ISO8859-7.pcf.gz

#%files 100dpi-ISO8859-8
#%defattr(644,root,root,755)
#%%{_fontsdir}/100dpi/*ISO8859-8.pcf.gz

%files 100dpi-ISO8859-9
%defattr(644,root,root,755)
%{_fontsdir}/100dpi/*ISO8859-9.pcf.gz

%files 100dpi-ISO8859-10
%defattr(644,root,root,755)
%{_fontsdir}/100dpi/*ISO8859-10.pcf.gz

#%files 100dpi-ISO8859-11
#%defattr(644,root,root,755)
#%%{_fontsdir}/100dpi/*ISO8859-11.pcf.gz

#%files 100dpi-ISO8859-12
#%defattr(644,root,root,755)
#%%{_fontsdir}/100dpi/*ISO8859-12.pcf.gz

%files 100dpi-ISO8859-13
%defattr(644,root,root,755)
%{_fontsdir}/100dpi/*ISO8859-13.pcf.gz

%files 100dpi-ISO8859-14
%defattr(644,root,root,755)
%{_fontsdir}/100dpi/*ISO8859-14.pcf.gz

%files 100dpi-ISO8859-15
%defattr(644,root,root,755)
%{_fontsdir}/100dpi/*ISO8859-15.pcf.gz

#%files 100dpi-JISX0201.1976-0
#%defattr(644,root,root,755)

#%files 100dpi-KOI8-R
#%defattr(644,root,root,755)

%files Ethiopic
%defattr(644,root,root,755)
%{_fontsdir}/OTF/GohaTibebZemen.otf
%{_fontsdir}/TTF/GohaTibebZemen.ttf

%files Syriac
%defattr(644,root,root,755)
%doc xc/fonts/scaled/Meltho/{README,license.txt}
%{_fontsdir}/OTF/SyrCOM*.otf

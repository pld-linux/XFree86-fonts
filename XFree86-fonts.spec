Summary:	XFree86 Fonts
Summary(pl):	Fonty dla systemu XFree86 
Name:		XFree86-fonts
Version:	4.0.2
Release:	2
License:	MIT
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Source0:	ftp://ftp.xfree86.org/pub/XFree86/4.0/source/X402src-2.tgz
Source1:	ftp://ftp.xfree86.org/pub/XFree86/4.0/source/X402src-1.tgz
Source2:	http://www.biz.net.pl/images/ISO8859-2-bdf.tar.gz
Source3:	ftp://crash.fce.vutbr.cz/pub/linux_fonts/TGZ/ulT1mo-beta-1.0.tgz
Patch0:		%{name}-extras-fix.patch
Patch1:		%{name}-ISO8859-2.patch
BuildRequires:	XFree86 = %{version}
BuildRequires:	XFree86-devel = %{version}
Prereq:		/usr/X11R6/bin/mkfontdir
Obsoletes:	XFree86-latin2-fonts
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_fontdir	/usr/share/fonts
%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man
%define		_appnkldir	%{_datadir}/applnk

%description
This package contains the basic fonts. This package is required when
you have installed X server.

%description -l pl
Pakiet ten zawiera podstawowe czcionki. Pakiet ten jest koniecznie
potrzebny, je�li masz zainstalowany jakikolwiek X serwer.

%package utils
Summary:	Perl scripts for generating BDF fonts
Summary(pl):	Skrypty perlowe do generowania font�w BDF
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86

%description utils
Perl scripts that allow to generate from an ISO10646-1 encoded
BDF font other BDF fonts in any possible encoding.

%package -n XFree86-75dpi-fonts
Summary:	X11R6 75dpi fonts - only need on server side
Summary(de):	X11RT 76 dpi-Fonts - nur auf Serverseite erforderlich
Summary(fr):	Fontes 75 dpi X11R6 - n�cessaire uniquement c�t� serveur
Summary(pl):	Fonty o rozdzielczo�ci 75dpi - potrzebne tylko po stronie serwera
Summary(tr):	X11R6 75dpi yaz�tipleri - yaln�zca sunucu taraf�nda gerekir
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Prereq:		%{_bindir}/mkfontdir

%ifarch sparc
Obsoletes:	X11R6.1-75dpi-fonts
%endif

%description -n XFree86-75dpi-fonts
The 75dpi fonts used on most Linux systems. Users with high resolution
displays may prefer the 100dpi fonts available in a separate package.

%description -l de -n XFree86-75dpi-fonts
Die 75dpi-Fonts, die auf meisten Linux-Systemen verwendet werden. F�r
Benutzer mit einer hochaufl�sender Darstellung sind die 100dpi-Fonts
eines getrennt erh�ltlichen Pakets besser geeignet.

%description -l fr -n XFree86-75dpi-fonts
Fontes 75 dpi utilis�es sur la plupart des syst�mes Linux. Ceux qui
ont des �crans � haute r�solution pr�f�reront les fontes 100 dpi
disponibles dans un autre paquetage.

%description -l pl -n XFree86-75dpi-fonts
Pakiet ten zawiera czcionki rastrowe 75dpi. W wypadku wi�kszej
rozdzielczo�ci zalecane s� czcionki 100dpi, kt�re s� dost�pne w
osobnym pakiecie.

%description -l tr -n XFree86-75dpi-fonts
�o�u Linux sisteminde 75dpi yaz�tipi kullan�l�r. Y�ksek ��z�n�rl�k
kullanan kullan�c�lar 100dpi yaz�tiplerini ye�leyebilirler.

%package -n XFree86-100dpi-fonts
Summary:	X11R6 100dpi fonts - only need on server side
Summary(de):	X11R6 100dpi-Fonts - nur auf Server-Seite erforderlich
Summary(fr):	Fontes 100ppp pour X11R6 - n�cessaires seulement cot� serveur.
Summary(pl):	Fonty o rozdzielczosci 100dpi - potrzebne tylko po stronie serwera
Summary(tr):	X11R6 100dpi yaz�tipleri - yaln�zca sunucu taraf�nda gereklidir
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Prereq:		%{_bindir}/mkfontdir

%ifarch sparc
Obsoletes:	X11R6.1-100dpi-fonts
%endif

%description -n XFree86-100dpi-fonts
The 100dpi fonts used on most Linux systems. Users with high
resolution displays may prefer the 100dpi fonts available in a
separate package.

%description -l de -n XFree86-100dpi-fonts
Die 100dpi-Schriftarten, die auf den meisten Linux-Systemen zum
Einsatz kommen. Anwender mit hochaufl�senden Monitoren ziehen unter
Umst�nden die 100dpi-Schriften vor, die in einem separaten Paket
erh�ltlich sind.

%description -l fr -n XFree86-100dpi-fonts
Les fontes 100dpi sont utilis�es par la plupart des syst�mes Linux.
Les utilisateurs ayant des hautes r�solutions peuvent pr�f�rer les
fontes 100dpi disponibles dans un package s�par�.

%description -l pl -n XFree86-100dpi-fonts
Pakiet ten zawiera czcionki rastrowe 100dpi. Bed� one potrzebne przy
pracy w du�ych rozdzielczo�ciach.

%description -l tr -n XFree86-100dpi-fonts
Y�ksek ��z�n�rl�k kullanan kullan�c�lar 100dpi yaz�tiplerini 75dpi
olanlara ye�leyebilirler.

%package -n XFree86-cyrillic-fonts
Summary:	Cyrillic fonts - only need on server side
Summary(pl):	Fonty rastrowe z cyrylic�
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Prereq:		%{_bindir}/mkfontdir

%description -n XFree86-cyrillic-fonts
Cyrillic raster fonts.

%description -l pl -n XFree86-cyrillic-fonts
Fonty rastrowe z cyrylic�.

%package -n XFree86-latin2-100dpi-fonts
Summary:	Latin 2 100dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-2 o rozdzielczo�ci 100dpi
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Prereq:		%{_bindir}/mkfontdir
Obsoletes:	XFree86-ISO8859-2-100dpi-fonts

%description -n XFree86-latin2-100dpi-fonts
Latin 2 raster fonts.

%description -l pl -n XFree86-latin2-100dpi-fonts
Fonty rastrowe ISO-8859-2 o rozdzielczo�ci 100dpi.

%package -n XFree86-latin2-75dpi-fonts
Summary:	Latin 2 75dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-2 o rozdzielczo�ci 75dpi
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Prereq:		%{_bindir}/mkfontdir
Obsoletes:	XFree86-ISO8859-2-75dpi-fonts

%description -n XFree86-latin2-75dpi-fonts
Latin 2 raster fonts.

%description -l pl -n XFree86-latin2-75dpi-fonts
Fonty rastrowe ISO-8859-2 o rozdzielczo�ci 75dpi.

%package -n XFree86-latin2-Type1-fonts
Summary:	Type1 (scalable) ISO8859-2 X11 system fonts
Summary(pl):	Fonty Type 1 ISO-8859-2
Group:		X11/Fonts
Group(de):	X11/Fonts
Group(pl):	X11/Fonty
Prereq:		type1inst
Prereq:		/usr/bin/type1inst
Prereq:		textutils
Requires:	XFree86 > 3.2 
Requires:	type1inst >= 0.6.1
Obsoletes:	XFree86-ISO8859-2-Type1-fonts

%description -n XFree86-latin2-Type1-fonts
This package includes the Central European (ISO-8859-2) Type1 fonts
for the X11 system.

This is the famous ulT1mo (read ultimo) collection. All fonts are
copyrighted to their authors and declared to be freeware. Originals
was taken from the net or CDs.

%description -n XFree86-latin2-Type1-fonts -l pl
Pakiet ten zawiera zestaw font�w Type 1 ISO-8859-2 dla X Window.

%prep
%setup -q -c -b1 -b2 -a3
%patch0 -p1
%patch1 -p1

cp xc/extras/fonts/arabic24/*.bdf xc/fonts/bdf/misc/
cp xc/extras/fonts/ClearlyU/*.bdf xc/fonts/bdf/misc/

cd misc
for i in {12x24,8x16}*.bdf ; do
	mv $i "`echo $i | sed 's/\.bdf//'`-ISO8859-2.bdf"
done
cd ..
mv -f misc/{12x24,8x16}*.bdf xc/fonts/bdf/misc/
mv -f 100dpi/{char,term,lutBS,lutRS}* xc/fonts/bdf/latin2/100dpi/
mv -f 75dpi/{char,term,ncenR{18,24},lutBS{08,19,24},lutRS{08,19,24}}* xc/fonts/bdf/latin2/75dpi/

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
	CDEBUGFLAGS="$RPM_OPT_FLAGS"

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
	FONTDIR=$RPM_BUILD_ROOT%{_fontdir}

# make TrueType font dir, touch default .dir and .scale files
install	-d $RPM_BUILD_ROOT%{_fontdir}/TTF
echo 0 > $RPM_BUILD_ROOT%{_fontdir}/TTF/fonts.dir
echo 0 > $RPM_BUILD_ROOT%{_fontdir}/TTF/fonts.scale

gzip -9nf RELEASE_NOTES.TXT

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_fontdir}/misc
%{_bindir}/mkfontdir

%postun
cd %{_fontdir}/misc
umask 022
%{_bindir}/mkfontdir

%post -n XFree86-75dpi-fonts
cd %{_fontdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%postun -n XFree86-75dpi-fonts
cd %{_fontdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%post -n XFree86-100dpi-fonts
cd %{_fontdir}/100dpi
%{_bindir}/mkfontdir

%postun -n XFree86-100dpi-fonts
cd %{_fontdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%post -n XFree86-cyrillic-fonts
cd %{_fontdir}/cyrillic
%{_bindir}/mkfontdir

%post -n XFree86-latin2-100dpi-fonts
cd %{_fontdir}/latin2/100dpi
%{_bindir}/mkfontdir

%post -n XFree86-latin2-75dpi-fonts
cd %{_fontdir}/latin2/75dpi
%{_bindir}/mkfontdir

%post -n XFree86-latin2-Type1-fonts
cd %{_fontdir}/Type1
rm -f fonts.dir fonts.scale
/usr/bin/type1inst -nogs -nolog -q
grep '^.*ISO-8859-2.pfb' %{_fontdir}/Type1/fonts.dir |\
sed 's/\(^.*ISO-8859-2.pfb \)\(.*\)/"\2"/' |\
sed 's/\(^".*\)\(-[a-z]*-[a-z]*"\)/\1-iso8859-2" \1\2/' |\
grep -v ^[0-9] > %{_fontdir}/Type1/fonts.alias.tmp
cat %{_fontdir}/Type1/fonts.alias.tmp >>\
%{_fontdir}/Type1/fonts.alias
sort < %{_fontdir}/Type1/fonts.alias | uniq >\
%{_fontdir}/Type1/fonts.alias.tmp
mv -f %{_fontdir}/Type1/fonts.alias.tmp %{_fontdir}/Type1/fonts.alias

%postun -n XFree86-latin2-Type1-fonts
cd %{_fontdir}/Type1
rm -f fonts.dir fonts.scale
/usr/bin/type1inst -nogs -nolog -q
sed 's/^.*pfb -//' %{_fontdir}/Type1/fonts.dir > \
%{_fontdir}/Type1/fonts.dir.tmp 
grep -f %{_fontdir}/Type1/fonts.dir.tmp \
%{_fontdir}/Type1/fonts.alias > \
%{_fontdir}/Type1/fonts.alias.tmp
mv -f %{_fontdir}/Type1/fonts.alias.tmp %{_fontdir}/Type1/fonts.alias
rm -f %{_fontdir}/Type1/fonts.dir.tmp

%files
%defattr(644,root,root,755)
%doc RELEASE_NOTES.TXT.gz
%dir %{_fontdir}/CID
%dir %{_fontdir}/PEX
%dir %{_fontdir}/Speedo
%dir %{_fontdir}/TTF
%dir %{_fontdir}/encodings
%dir %{_fontdir}/local
%dir %{_fontdir}/Type1
%dir %{_fontdir}/misc
%{_fontdir}/PEX/*
%{_fontdir}/Speedo/*.spd
%{_fontdir}/encodings/*
%{_fontdir}/misc/*gz
%{_fontdir}/Type1/*[a-z_].*f*
%verify(not mtime size md5) %{_fontdir}/CID/fonts.*
%verify(not mtime size md5) %{_fontdir}/Speedo/fonts.*
%verify(not mtime size md5) %{_fontdir}/TTF/fonts.*
%verify(not mtime size md5) %{_fontdir}/local/fonts.*
%verify(not mtime size md5) %{_fontdir}/Type1/fonts.*
%verify(not mtime size md5) %{_fontdir}/misc/fonts.*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_fontdir}/util

%files -n XFree86-75dpi-fonts
%defattr(644,root,root,755)
%dir %{_fontdir}/75dpi
%{_fontdir}/75dpi/*gz
%verify(not mtime size md5) %{_fontdir}/75dpi/fonts.*

%files -n XFree86-100dpi-fonts
%defattr(644,root,root,755)
%dir %{_fontdir}/100dpi
%{_fontdir}/100dpi/*gz
%verify(not mtime size md5) %{_fontdir}/100dpi/fonts.*

%files -n XFree86-cyrillic-fonts
%defattr(644,root,root,755)
%{_fontdir}/cyrillic

%files -n XFree86-latin2-100dpi-fonts
%defattr(644,root,root,755)
%{_fontdir}/latin2/100dpi

%files -n XFree86-latin2-75dpi-fonts
%defattr(644,root,root,755)
%{_fontdir}/latin2/75dpi

%files -n XFree86-latin2-Type1-fonts
%defattr(644,root,root,755)
%{_fontdir}/Type1/afm/*
%{_fontdir}/Type1/pfm/*
%{_fontdir}/Type1/*-ISO-8859-2*

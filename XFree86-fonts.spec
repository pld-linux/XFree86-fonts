Summary:	XFree86 Fonts
Summary(pl):	Fonty dla systemu XFree86 
Name:		XFree86-fonts
Version:	4.0.3
Release:	1
License:	MIT
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Source0:	ftp://ftp.xfree86.org/pub/XFree86/4.0/source/X402src-2.tgz
Source1:	ftp://ftp.xfree86.org/pub/XFree86/4.0/source/X402src-1.tgz
Source2:	http://www.biz.net.pl/images/ISO8859-2-bdf.tar.gz
Source3:	ftp://crash.fce.vutbr.cz/pub/linux_fonts/TGZ/ulT1mo-beta-1.0.tgz
Source4:	%{name}.Fontmap
Source5:	%{name}-latin2-Type1.Fontmap
Patch0:		%{name}-extras-fix.patch
Patch1:		%{name}-ISO8859-2.patch
Patch2:		ftp://ftp.xfree86.org/pub/XFree86/4.0.3/patches/4.0.2-4.0.3.diff.gz
BuildRequires:	XFree86 = %{version}
BuildRequires:	XFree86-devel = %{version}
BuildRequires:	perl
BuildRequires:	t1utils
Prereq:		/usr/X11R6/bin/mkfontdir
Prereq:		textutils
Prereq:		sed
Obsoletes:	XFree86-latin2-fonts
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
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
Group(de):	X11/XFree86
Group(pl):	X11/XFree86

%description utils
Perl scripts that allow to generate from an ISO10646-1 encoded
BDF font other BDF fonts in any possible encoding.

%package -n XFree86-75dpi-fonts
Summary:	X11R6 75dpi fonts - only need on server side
Summary(de):	X11RT 75 dpi-Fonts - nur auf Serverseite erforderlich
Summary(fr):	Fontes 75 dpi X11R6 - nécessaire uniquement côté serveur
Summary(pl):	Fonty o rozdzielczo¶ci 75dpi - potrzebne tylko po stronie serwera
Summary(tr):	X11R6 75dpi yazýtipleri - yalnýzca sunucu tarafýnda gerekir
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
Die 75dpi-Fonts, die auf meisten Linux-Systemen verwendet werden. Für
Benutzer mit einer hochauflösender Darstellung sind die 100dpi-Fonts
eines getrennt erhältlichen Pakets besser geeignet.

%description -l fr -n XFree86-75dpi-fonts
Fontes 75 dpi utilisées sur la plupart des systèmes Linux. Ceux qui
ont des écrans à haute résolution préfèreront les fontes 100 dpi
disponibles dans un autre paquetage.

%description -l pl -n XFree86-75dpi-fonts
Pakiet ten zawiera czcionki rastrowe 75dpi. W wypadku wiêkszej
rozdzielczo¶ci zalecane s± czcionki 100dpi, które s± dostêpne w
osobnym pakiecie.

%description -l tr -n XFree86-75dpi-fonts
Çoðu Linux sisteminde 75dpi yazýtipi kullanýlýr. Yüksek çözünürlük
kullanan kullanýcýlar 100dpi yazýtiplerini yeðleyebilirler.

%package -n XFree86-100dpi-fonts
Summary:	X11R6 100dpi fonts - only need on server side
Summary(de):	X11R6 100dpi-Fonts - nur auf Server-Seite erforderlich
Summary(fr):	Fontes 100ppp pour X11R6 - nécessaires seulement coté serveur.
Summary(pl):	Fonty o rozdzielczosci 100dpi - potrzebne tylko po stronie serwera
Summary(tr):	X11R6 100dpi yazýtipleri - yalnýzca sunucu tarafýnda gereklidir
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
Einsatz kommen. Anwender mit hochauflösenden Monitoren ziehen unter
Umständen die 100dpi-Schriften vor, die in einem separaten Paket
erhältlich sind.

%description -l fr -n XFree86-100dpi-fonts
Les fontes 100dpi sont utilisées par la plupart des systèmes Linux.
Les utilisateurs ayant des hautes résolutions peuvent préférer les
fontes 100dpi disponibles dans un package séparé.

%description -l pl -n XFree86-100dpi-fonts
Pakiet ten zawiera czcionki rastrowe 100dpi. Bed± one potrzebne przy
pracy w du¿ych rozdzielczo¶ciach.

%description -l tr -n XFree86-100dpi-fonts
Yüksek çözünürlük kullanan kullanýcýlar 100dpi yazýtiplerini 75dpi
olanlara yeðleyebilirler.

%package -n XFree86-cyrillic-fonts
Summary:	Cyrillic fonts - only need on server side
Summary(pl):	Fonty rastrowe z cyrylic±
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Prereq:		%{_bindir}/mkfontdir

%description -n XFree86-cyrillic-fonts
Cyrillic raster fonts.

%description -l pl -n XFree86-cyrillic-fonts
Fonty rastrowe z cyrylic±.

%package -n XFree86-latin2-100dpi-fonts
Summary:	Latin 2 100dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-2 o rozdzielczo¶ci 100dpi
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Prereq:		%{_bindir}/mkfontdir
Obsoletes:	XFree86-ISO8859-2-100dpi-fonts

%description -n XFree86-latin2-100dpi-fonts
Latin 2 raster fonts.

%description -l pl -n XFree86-latin2-100dpi-fonts
Fonty rastrowe ISO-8859-2 o rozdzielczo¶ci 100dpi.

%package -n XFree86-latin2-75dpi-fonts
Summary:	Latin 2 75dpi fonts - only need on server side
Summary(pl):	Fonty rastrowe ISO-8859-2 o rozdzielczo¶ci 75dpi
Group:		X11/XFree86
Group(de):	X11/XFree86
Group(pl):	X11/XFree86
Prereq:		%{_bindir}/mkfontdir
Obsoletes:	XFree86-ISO8859-2-75dpi-fonts

%description -n XFree86-latin2-75dpi-fonts
Latin 2 raster fonts.

%description -l pl -n XFree86-latin2-75dpi-fonts
Fonty rastrowe ISO-8859-2 o rozdzielczo¶ci 75dpi.

%package -n XFree86-latin2-Type1-fonts
Summary:	Type1 (scalable) ISO8859-2 X11 system fonts
Summary(pl):	Fonty Type 1 ISO-8859-2
Group:		X11/Fonts
Group(de):	X11/Fonts
Group(pl):	X11/Fonty
Prereq:		textutils
Prereq:		sed
Requires:	XFree86 > 3.2 
Obsoletes:	XFree86-ISO8859-2-Type1-fonts

%description -n XFree86-latin2-Type1-fonts
This package includes the Central European (ISO-8859-2) Type1 fonts
for the X11 system.

This is the famous ulT1mo (read ultimo) collection. All fonts are
copyrighted to their authors and declared to be freeware. Originals
was taken from the net or CDs.

%description -n XFree86-latin2-Type1-fonts -l pl
Pakiet ten zawiera zestaw fontów Type1 ISO-8859-2 dla X Window.

%prep
%setup -q -c -b1 -b2 -a3
%patch0 -p1
%patch1 -p1
%patch2 -p0

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

tail -n +2 ulT1mo-beta-1.0/fonts.scale.ulT1mo \
	> $RPM_BUILD_ROOT%{_t1fontsdir}/fonts.scale.XFree86-latin2-Type1-fonts
tail -n +2 xc/fonts/scaled/Type1/fonts.scale | sed -e 's/\.pfa/\.pfb/' \
	> $RPM_BUILD_ROOT%{_t1fontsdir}/fonts.scale.%{name}
install %{SOURCE4} $RPM_BUILD_ROOT%{_t1fontsdir}/Fontmap.%{name}
install %{SOURCE5} $RPM_BUILD_ROOT%{_t1fontsdir}/Fontmap.XFree86-latin2-Type1-fonts

# make TrueType font dir, touch default .dir and .scale files
install	-d $RPM_BUILD_ROOT%{_fontsdir}/TTF
echo 0 > $RPM_BUILD_ROOT%{_fontsdir}/TTF/fonts.dir
echo 0 > $RPM_BUILD_ROOT%{_fontsdir}/TTF/fonts.scale

gzip -9nf RELEASE_NOTES.TXT

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir
cd %{_t1fontsdir}
rm -f fonts.scale.bak Fontmap.bak
cat fonts.scale.* | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp
ln -sf fonts.scale fonts.dir
cat Fontmap.* > Fontmap

%postun
cd %{_fontsdir}/misc
umask 022
%{_bindir}/mkfontdir
cd %{_t1fontsdir}
rm -f fonts.scale.bak Fontmap.bak
cat fonts.scale.* 2>/dev/null | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp
ln -sf fonts.scale fonts.dir
cat Fontmap.* > Fontmap 2>/dev/null

%post -n XFree86-75dpi-fonts
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%postun -n XFree86-75dpi-fonts
cd %{_fontsdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%post -n XFree86-100dpi-fonts
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%postun -n XFree86-100dpi-fonts
cd %{_fontsdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%post -n XFree86-cyrillic-fonts
cd %{_fontsdir}/cyrillic
umask 022
%{_bindir}/mkfontdir

%post -n XFree86-latin2-100dpi-fonts
cd %{_fontsdir}/latin2/100dpi
umask 022
%{_bindir}/mkfontdir

%post -n XFree86-latin2-75dpi-fonts
cd %{_fontsdir}/latin2/75dpi
umask 022
%{_bindir}/mkfontdir

%post -n XFree86-latin2-Type1-fonts
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

%postun -n XFree86-latin2-Type1-fonts
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

%files
%defattr(644,root,root,755)
%doc RELEASE_NOTES.TXT.gz
%dir %{_fontsdir}/CID
%dir %{_fontsdir}/PEX
%dir %{_fontsdir}/Speedo
%dir %{_fontsdir}/TTF
%dir %{_fontsdir}/encodings
%dir %{_fontsdir}/local
%dir %{_fontsdir}/misc
%{_fontsdir}/PEX/*
%{_fontsdir}/Speedo/*.spd
%{_fontsdir}/encodings/*
%{_fontsdir}/misc/*gz
%{_t1fontsdir}/*[a-z_].pfb
%{_t1afmdir}/*[a-z_].afm
%{_t1fontsdir}/*.%{name}
%verify(not mtime size md5) %{_fontsdir}/CID/fonts.*
%verify(not mtime size md5) %{_fontsdir}/Speedo/fonts.*
%verify(not mtime size md5) %{_fontsdir}/TTF/fonts.*
%verify(not mtime size md5) %{_fontsdir}/local/fonts.*
%verify(not mtime size md5) %{_fontsdir}/misc/fonts.*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_fontsdir}/util

%files -n XFree86-75dpi-fonts
%defattr(644,root,root,755)
%dir %{_fontsdir}/75dpi
%{_fontsdir}/75dpi/*gz
%verify(not mtime size md5) %{_fontsdir}/75dpi/fonts.*

%files -n XFree86-100dpi-fonts
%defattr(644,root,root,755)
%dir %{_fontsdir}/100dpi
%{_fontsdir}/100dpi/*gz
%verify(not mtime size md5) %{_fontsdir}/100dpi/fonts.*

%files -n XFree86-cyrillic-fonts
%defattr(644,root,root,755)
%{_fontsdir}/cyrillic

%files -n XFree86-latin2-100dpi-fonts
%defattr(644,root,root,755)
%{_fontsdir}/latin2/100dpi

%files -n XFree86-latin2-75dpi-fonts
%defattr(644,root,root,755)
%{_fontsdir}/latin2/75dpi

%files -n XFree86-latin2-Type1-fonts
%defattr(644,root,root,755)
%{_t1fontsdir}/*-ISO-8859-2*
%{_t1afmdir}/*-ISO-8859-2*.afm
%{_t1pfmdir}/*-ISO-8859-2*.pfm
%{_t1fontsdir}/*.XFree86-latin2-Type1-fonts

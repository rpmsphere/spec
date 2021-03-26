%global debug_package %{nil}
%global _name scid_vs_pc
%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}

Name:           scidvspc
Version:        4.21
Release:        1
Summary:        A chess database application
License:        GPLv2+
URL:            http://sourceforge.net/projects/scidvspc
Source0:        https://sourceforge.net/projects/scidvspc/files/source/%{_name}-%{version}.tgz
Source1:        %{name}.desktop
BuildRequires:  tk-devel
BuildRequires:  tcl
BuildRequires:  desktop-file-utils
BuildRequires:  libX11
BuildRequires:  libstdc++-devel
Requires:       tcl
Requires:       tk

%description
Shane's Chess Information Database is a huge chess toolkit with extensive
database, analysis, and chess-playing features.

Scid vs. PC is a usability and bug-fix fork of Scid. It has extensive interface
fixes and improvements and is fully compatible with Scid's .si4 databases.
Its new features include a rewitten Gamelist, a Computer Tournament, and FICS,
Tree, and Book improvements.

%package sounds
Summary:        Sounds for %{_name}
License:        GPLv2+
BuildArch:      noarch
Requires:       tcl-snack
Requires:       %{name} = %{version}-%{release}

%description sounds
This package contains sounds for %{_name}.

%package books
Summary:        Opening books for %{_name}
License:        GPLv2+ and freely redistributable
# books/{Performance.bin,varied.bin} are freely redistributable
# books/{Elo2400.bin,gm2600.bin} are GPL
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description books
This package contains opening books for %{_name}.

%prep
%setup -q -n %{_name}-%{version}
sed -i 's|/tkscid|/%{name}_tkscid|' scripts/sc_remote.tk tcl/start.tcl

for file in engines/toga/readme.txt; do
    mv $file timestamp
    iconv -f ISO-8859-1 -t UTF-8 -o $file timestamp
    touch -r timestamp $file
    rm -f timestamp
done

%build
./configure \
        OPTIMIZE="%{optflags}" \
        BINDIR=%{_bindir} \
        SHAREDIR=%{_datadir}/%{name} \
        TCL_LIBRARY="-ltcl%{tcl_version}" \
        TK_LIBRARY="-ltk%{tcl_version} -ltcl%{tcl_version}"

# BASH_ENV messes with the include path and with GCC 6 (F24+)
# messing with the include path causes stdlib.h to not be
# found.  See https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/37NHYB3UYTO7K53N3H535MUNVCIDGT3O/
make WARNINGS='-w' LDFLAGS='-lX11' BASH_ENV=''

%install
mkdir -p %{buildroot}/%{_docdir}/%{name}/ezsmtp
mkdir -p %{buildroot}/%{_licensedir}/%{name}/ezsmtp
mv tcl/contrib/ezsmtp/{ChangeLog,ezsmtp.html,koi8-r-body.txt,README.txt,test_examples.txt} %{buildroot}/%{_docdir}/%{name}/ezsmtp
mv tcl/contrib/ezsmtp/license.txt %{buildroot}/%{_licensedir}/%{name}/ezsmtp

make DESTDIR=%{buildroot} install

desktop-file-install \
        --dir %{buildroot}/%{_datadir}/applications \
        %{SOURCE1}

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/
install -m 644 -p icons/scid.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/sounds/
install -m 644 -p sounds/*.wav %{buildroot}/%{_datadir}/%{name}/sounds/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/images/
install -m 644 -p images/* %{buildroot}/%{_datadir}/%{name}/images/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/photos/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/fonts
install -m 644 -p fonts/*.ttf %{buildroot}/%{_datadir}/%{name}/fonts/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/bitmaps/
install -m 644 -p bitmaps/*.gif %{buildroot}/%{_datadir}/%{name}/bitmaps/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/bitmaps2/
install -m 644 -p bitmaps2/*.gif %{buildroot}/%{_datadir}/%{name}/bitmaps2/

mv COPYING %{buildroot}/%{_licensedir}/%{name}
mkdir %{buildroot}/%{_docdir}/%{name}/{toga,phalanx}
mkdir %{buildroot}/%{_licensedir}/%{name}/{toga,phalanx}

mv engines/toga/readme.txt %{buildroot}/%{_docdir}/%{name}/toga
mv engines/toga/copying.txt %{buildroot}/%{_licensedir}/%{name}/toga
mv engines/phalanx/{HISTORY,README} %{buildroot}/%{_docdir}/%{name}/phalanx
mv engines/phalanx/COPYING %{buildroot}/%{_licensedir}/%{name}/phalanx

# Rename various executables to prevent RPM conflicts with original SCID
cd %{buildroot}/%{_bindir}
for i in *
do
mv $i %{name}_$i
done

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
update-desktop-database &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%{_docdir}/%{name}
%{_licensedir}/%{name}
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/sounds
%exclude %{_datadir}/%{name}/books
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/128x128/apps/*
%{_datadir}/fonts/truetype/Scid

%files sounds
%{_datadir}/%{name}/sounds

%files books
%{_datadir}/%{name}/books/*.bin
%doc books/readme.txt

%changelog
* Tue Jan 07 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 4.21
- Rebuild for Fedora
* Mon Apr 25 2016 Alex Wood <awood@redhat.com> 4.16-3
- Apply patch to address crashes with Stockfish. See BZ 1325013.
* Thu Mar 31 2016 Alex Wood <awood@redhat.com> 4.16-2
- Rename files that conflict with files in the original SCID.
* Tue Mar 29 2016 Alex Wood <awood@redhat.com> 4.16-1
- Initial packaging.  Spec file adopted from original SCID spec.

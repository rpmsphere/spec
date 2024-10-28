%undefine _debugsource_packages

Summary:        A strong chess engine using the winboard protocol
Name:           sloppy
Version:        0.2.2
Release:        12.1
License:        GPL v3
Group:          Amusements/Games/Board/Chess
URL:            https://ilaripih.mbnet.fi/sloppy/
Source0:        sloppy-%{version}.tar.bz2
Source1:        xsloppy
# startup script derived from script by Oliver Korff
Source2:        %{name}.sh
Source3:        book.bin.bz2
Source4:        %{name}.sh
Patch0:         %{name}-config.patch
Patch1:         sloppy-no-build-date.patch
Requires:       xboard

%description
Sloppy is a versatile open source chess engine written by some Finnish dude.  
Here are some facts about Sloppy:
- Written in C, or more precisely, the C99 version of C
- Uses the Xboard/Winboard chess engine communication protocol version 2
- Should compile on most PC or Mac platforms (eg. Linux, Windows, OS X)
- Licensed under version 3 of the GNU General Public Licence
- Often plays in a way which could be described as sloppy

Authors:
                Ilari Pihlajisto <ilari.pihlajisto@mbnet.fi>

%prep
%setup -q
%patch 0 -p0
%patch 1 -p1
%ifarch aarch64
sed -i '479,494d' src/util.c
%endif

%build
cd src
make

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 755 src/sloppy $RPM_BUILD_ROOT%{_bindir}/%{name}.bin
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/xsloppy
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m 644 sloppy.conf $RPM_BUILD_ROOT%{_datadir}/%{name}/
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/%{name}/
bzip2 -d $RPM_BUILD_ROOT%{_datadir}/%{name}/book.bin.bz2

%files
%doc CHANGES  COPYING  README TODO 
%{_bindir}/*%{name}*
%{_datadir}/%{name}

%changelog
* Tue Sep 12 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.2
- Rebuilt for Fedora
* Thu Aug 27 2009 AxelKoellhofer@web.de
- first build for openSUSE, version 0.2.2

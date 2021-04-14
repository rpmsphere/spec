Name: wiznote
Summary: Qt client for WizNote
Version: 2.7.1
Release: 1
Group: Applications/Editors
License: GPLv3
URL: https://github.com/WizTeam/WizQTClient
#Source0: WizQTClient-%{version}.tar.gz
Source0: WizQTClient-master.zip
BuildRequires: cmake, qt5-devel, qt5-qtwebkit-devel

%description
A cross-platform client written in Qt for the Wiz Note.

%prep
#setup -q -n WizQTClient-%{version}
%setup -q -n WizQTClient-master

%build
#cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS=-Wno-narrowing .
#sed -i 's|CXXFLAGS =|CXXFLAGS = -Wno-narrowing|' lib/cryptopp/GNUmakefile
#sed -i 's|isystem |I|' `find . -name flags.make`
%cmake -DCMAKE_BUILD_TYPE=Release
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
mv %{buildroot}%{_bindir}/WizNote %{buildroot}%{_bindir}/%{name}

%files
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}
#{_libdir}/%{name}
%{_datadir}/licenses/%{name}

%changelog
* Wed Aug 14 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.7.1
- Rebuilt for Fedora

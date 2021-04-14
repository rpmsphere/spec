Name:           pmetro-maps
Version:        0.0
Release:        9
License:        GPL-2.0+
Summary:        Maps for Metromap
URL:            http://pmetro.su/Maps.html
Group:          Productivity/Other
#Source:        http://pmetro.su/*.zip
Source:         MetroPack.zip
#Requires:       metromap | qmetro
BuildRequires:  unzip
BuildArch:      noarch

%description
Maps for the metromap/qmetro program.

%prep
%setup -q -c
unzip -o '*.zip'

%build
#rm Berlin.pmz Kiev.pmz London.pmz Moscow.pmz New-York.pmz Paris.pmz Peterburg.pmz

%install
install -dm 0755 $RPM_BUILD_ROOT%{_datadir}/pmetro-maps
install -m 0644 *.pmz $RPM_BUILD_ROOT%{_datadir}/pmetro-maps

%files
%{_datadir}/pmetro-maps

%changelog
* Sun Apr 11 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0
- Rebuilt for Fedora
* Sat Jun  2 2012 lazy.kent@opensuse.org
- Updated maps:
  * Kazan
  * Moscow
  * Saint Petersburg
* Fri May 18 2012 lazy.kent@opensuse.org
- Updated maps:
  * Baku
  * Moscow
  * Saint Petersburg

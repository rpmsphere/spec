Name:           fortune-it
Version:        1.99
Release:        3.1
Summary:        Collection of Italian fortune cookie files
Group:          Amusements/Games
License:        Public Domain
URL:            https://www.fortune-it.net/
Source0:        https://www.fortune-it.net/download/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  fortune-mod
Requires:       fortune-mod

%description
This package contains Italian Fortunes for Linux.
They are all in Italian language.  So, this package is interesting for
Italian people only (and for those who know Italian language, of course).

%prep
%setup -q

%build
cd testi
##Fedora doesn't like offensive cookies
rm -f *-o
for _file in *; do
  strfile $_file
done

%install
mkdir -p %{buildroot}%{_datadir}/fortune/it
cp testi/* %{buildroot}%{_datadir}/fortune/it

%files
%doc README COPYING
%{_datadir}/fortune/it

%changelog
* Wed May 06 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.99
- Rebuilt for Fedora
* Mon Jan 14 2013 Simone Sclavi <darkhado@gmail.com> - 1.99-1
- Initial build


Name: izulu
Summary: Change the wallpaper according to the weather
Version: 0.5
Release: 4.1
Group: Amusements/Graphics
License: GPL
URL: https://onli.github.io/izulu/
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: gettext
Requires: xmlstarlet
Requires: perl-XML-Twig
Requires: ImageMagick
Requires: wget

%description
izulu is a script which changes the background of your GNU/Linux-Desktop
according to the weather.

%prep
%setup -q
sed -i '1i msgid ""\nmsgstr "Content-Type: text/plain; charset=UTF-8"' lang/*.po

%build
make

%install
%make_install
rm %{buildroot}%{_datadir}/doc/credits.txt

%files
%doc ChangeLog LICENSE README.md doc/credits.txt
%{_bindir}/%{name}
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Fri Mar 06 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuilt for Fedora

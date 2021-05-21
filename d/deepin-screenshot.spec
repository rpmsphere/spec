Name:           deepin-screenshot
Version:        2.0
Release:        2.1
Summary:        Screenshot tool from Deepin team
Group:          Productivity/Graphics/Other
License:        GPL-3.0
URL:            http://www.linuxdeepin.com/
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       deepin-ui >= 1.0

%description
Deepin Screenshot: a lightware screenshot tool
Features:
 - Automatic window identification
 - Selection of area
 - Editing screenshots
 - Saving to clipboard
 - Delayed shots

%prep
%setup -q

%build
./updateTranslate.sh

%install
%__install -d %{buildroot}%{_datadir}/%{name}/{locale,src,theme}

cp -r %{_builddir}/%{name}-%{version}/{src,theme,locale} %{buildroot}/%{_datadir}/%{name}/

%__install -D -m 644 %{_builddir}/%{name}-%{version}/{AUTHORS,README,ChangeLog} %{buildroot}/%{_datadir}/%{name}/

%__install -d %{buildroot}%{_bindir}
ln -s %{_datadir}/%{name}/src/%{name} %{buildroot}%{_bindir}/%{name}

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/%{name}
%dir /usr/share/%{name}
%{_datadir}/%{name}/theme
%{_datadir}/%{name}/src
%{_datadir}/%{name}/locale
%doc %{_datadir}/%{name}/AUTHORS
%doc %{_datadir}/%{name}/README
%doc %{_datadir}/%{name}/ChangeLog
%attr(755,root,root) %{_datadir}/%{name}/src/%{name}

%changelog
* Fri Jun 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuilt for Fedora
* Tue Aug 28 2012 nekolayer@yandex.ru
- initial package

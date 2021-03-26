Name:		ossii-menu
Version:	0.3
Release:	2
Summary:	Common menu for OSSII Linux
License:	GPL
Group:		User Interface/Desktops
Source:		%{name}-%{version}.zip
URL:		http://www.ossii.com.tw/
BuildArch:	noarch

%description
The purpose of ossii-menu is to patch the menu for OSSII Linux.
The function of software should be clear just through
it's name on this menu suitable for every Linux distribution.

%prep
%setup -q -c

%build

%install
%__rm -rf %{buildroot}
%__install -Dm 755 %{name}.sh %{buildroot}%{_bindir}/%{name}
%__install -Dm 755 %{name}-mkcsv.sh %{buildroot}%{_bindir}/%{name}-mkcsv
%__install -Dm 644 applications.csv %{buildroot}%{_datadir}/%{name}/applications.csv

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}*
%{_datadir}/%{name}

%changelog
* Fri Feb 25 2011 Wei-Lun Chao <bluebat@member.fsf.org> 0.3-1.ossii
- Add ossii-menu-mkcsv

* Tue Mar 03 2009 Wei-Lun Chao <bluebat@member.fsf.org> 0.2-1.ossii
- Fix bugs

* Mon Jan 05 2009 Wei-Lun Chao <bluebat@member.fsf.org> 0.1-1.ossii
- Initial package

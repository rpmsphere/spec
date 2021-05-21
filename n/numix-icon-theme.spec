%global theme	Numix

Name:		numix-icon-theme
Version:	2.3.2
Release:	2.1
Summary:	%{theme} icon theme
Group:		System/Configuration/Theme
License:	GPL-3
URL:		http://www.numixproject.org
Source0:	%{name}-master.tar.xz
BuildArch:	noarch

%description
%{theme} is an icon theme from the Numix project.

%prep
%setup -q -n %{name}-master

%build

%install
rm -rf %{buildroot}
%{__install} -d -m755 %{buildroot}%{_datadir}/icons/
%{__cp} -pr %{theme} %{buildroot}%{_datadir}/icons/

%files 
%{_datadir}/icons/%{theme}

%clean
rm -rf %{buildroot}

%changelog
* Wed Jul 08 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.2
- Rebuilt for Fedora
* Thu Oct 16 2014 Agent Smith <ruidobranco@yahoo.com.br> 2.3.2-1pclos2014
- Created package numix-icon-theme

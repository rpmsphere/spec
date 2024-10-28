%define theme_name SolarCity

Summary: %{theme_name} metacity theme
Name: solarcity-metacity-theme
Version: 0.3
Release: 4.1
License: GPL
Group: User Interface/Desktops
Source: https://themes.freshmeat.net/redir/solarcity/51649/url_tgz/solarcity-default-%{version}.tar.gz
URL: https://themes.freshmeat.net/projects/solarcity/
BuildArch: noarch

%description
%{theme_name} is a Motif-like theme for Metacity.

%prep
%setup -q -n %{theme_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -R * $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%files
%{_datadir}/themes/%{theme_name}

%changelog
* Thu Apr 21 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora

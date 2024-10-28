%global theme_name ACYLS
%global _python_bytecompile_errors_terminate_build 0

Summary:        Any Color You Like Simple icon theme
Name:           acyls-icon-theme
Version:        20161113
Release:        6.1
License:        GPL
Group:          User Interface/Desktops
URL:            https://www.gnome-look.org/p/1152587/
Source0:        https://dl.opendesktop.org/api/files/download/id/1479059924/ACYLS.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%description
Big fan of ACYL by switzak I made some improvements for better usability
and customization. I want make this work public since original theme
doesn't have any updates for a long time.

%package -n acyls
Summary: Config tool for the Any Color You Like Simple icon theme
Requires: %{name}
Requires: python3-lxml

%description -n acyls
Config tool for the Any Color You Like Simple icon theme.

%prep
%setup -q -n %{theme_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/acyls << EOF
#!/bin/bash
cd %{_datadir}/acyls/scripts
./run.py
EOF
chmod +x $RPM_BUILD_ROOT%{_bindir}/acyls
mkdir -p $RPM_BUILD_ROOT%{_datadir}/acyls
cp -a scripts $RPM_BUILD_ROOT%{_datadir}/acyls

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a scalable index.theme $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%files 
%{_datadir}/icons/%{theme_name}

%files -n acyls
%{_bindir}/acyls
%{_datadir}/acyls
#%{_datadir}/applications/acyl.desktop

%changelog
* Wed Jan 04 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 20161113
- Rebuilt for Fedora

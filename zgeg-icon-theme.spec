%define theme_name Zgeg

Summary: Zgeg icon theme
Name: zgeg-icon-theme
Version: 200805
Release: 1.1
License: GPL
Group: User Interface/Desktops
Source: zgeg-icon.zip
BuildArch: noarch

%description
Contains the Zgeg icon theme.

%prep
%setup -q -n %{theme_name}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/icons/%{theme_name}
cp -a * %{buildroot}%{_datadir}/icons/%{theme_name}

%clean
rm -rf %{buildroot}

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 200805
- Rebuild for Fedora

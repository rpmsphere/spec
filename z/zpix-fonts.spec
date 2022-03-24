%define	font_dir %{_datadir}/fonts/zpix

Name:           zpix-fonts
Summary:        Zpix FONTS
Version:        3.1.6
Release:        1
License:        shareware
Group:          User Interface/X
URL:            https://github.com/SolidZORO/zpix-pixel-font
Source0:        zpix-pixel-font-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  p7zip

%description
Zpix includes bitmap chinese fonts (embeded in ttf).

%prep
%setup -q -n zpix-pixel-font-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{font_dir}
install -m 644 dist/*.ttf $RPM_BUILD_ROOT%{font_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc *.md
%{font_dir}

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 3.1.6
- Rebuilt for Fedora

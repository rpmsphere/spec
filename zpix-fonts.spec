%define	font_dir %{_datadir}/fonts/zpix

Name:           zpix-fonts
Summary:        Zpix FONTS
Version:        2.0
Release:        8.1
License:        shareware
Group:          User Interface/X
URL:            https://github.com/SolidZORO/zpix-pixel-font
Source0:        http://zpix.googlecode.com/files/Zpix.zip
Source1:	    http://zpix.googlecode.com/files/ZpixC.O.D.E.7z
BuildArch:      noarch
BuildRequires:  p7zip

%description
Zpix includes bitmap chinese fonts (embeded in ttf).

%prep
%setup -q -c -a 1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{font_dir}
install -m 644 *.ttf $RPM_BUILD_ROOT%{font_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{font_dir}

%changelog
* Sun Jan 06 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuild for Fedora

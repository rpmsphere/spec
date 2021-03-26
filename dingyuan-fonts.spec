%define	fontdir	%{_datadir}/fonts/dingyuan

Name:           dingyuan-fonts
Version:        1.1.5.1411
Release:        2.1
Summary:        Chinese fonts by gumblex
License:        GPL
Group:          System/X11/Fonts
URL:            https://github.com/gumblex/
Source0:        dingyuan.zip
BuildArch:      noarch

%description
https://gumble.tk/dingyuanzhonghei.html
https://gumble.tk/stamico.html

%prep
%setup -q -c

%build

%install
install -d %{buildroot}%{fontdir}
install -m644 *.ttf %{buildroot}%{fontdir}

%files
%{fontdir}/*

%changelog
* Mon May 09 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.5.1411
- Rebuild for Fedora

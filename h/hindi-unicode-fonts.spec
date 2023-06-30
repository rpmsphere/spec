%define	fontdir	%{_datadir}/fonts/hindi-unicode

Name:           hindi-unicode-fonts
Version:        2.04
Release:        7.1
Summary:        Fonts for Hindi language
License:        GPL
Group:          System/X11/Fonts
URL:            https://fedora-art.org/usermanager/search.php?username=maarizwan&action=contents
Source0:        https://fedora-art.org/CONTENT/content-files/158726-Sadhguru-1.8.zip
Source1:        https://fedora-art.org/CONTENT/content-files/16645-Gurumaa-2.04.zip
Source2:        https://fedora-art.org/CONTENT/content-files/142684-Nithyananda-2.04.zip
Source3:        10-hindi-unicode.conf
BuildArch:      noarch

%description
https://fedora-art.org/content/show.php/Sadhguru+Hindi+Unicode+Font+-+v1.8?content=158726
https://fedora-art.org/content/show.php/Gurumaa+Hindi+Unicode+Font+%28GPL%29?content=16645
https://fedora-art.org/content/show.php/Nithyananda+Hindi+Unicode+Font+%28GPL%29?content=142684

%prep
%setup -q -c -a 1 -a 2

%build

%install
install -d %{buildroot}%{fontdir}
install -m644 Gurumaa-2.04/Gurumaa-2.04.ttf %{buildroot}%{fontdir}/Gurumaa.ttf
install -m644 Nithyananda-2.04/Nithyananda-2.04.ttf %{buildroot}%{fontdir}/Nithyananda.ttf
install -m644 Sadhguru-1.8/sadhguru-1.8.ttf %{buildroot}%{fontdir}/sadhguru.ttf
install -d %{buildroot}%{_docdir}/%{name}
install -m644 Gurumaa-2.04/README.txt %{buildroot}%{_docdir}/%{name}/Gurumaa.README
install -m644 Nithyananda-2.04/README.txt %{buildroot}%{_docdir}/%{name}/Nithyananda.README
install -m644 Sadhguru-1.8/README.txt %{buildroot}%{_docdir}/%{name}/sadhguru.README
install -m644 Sadhguru-1.8/Font-Exception-license.txt Sadhguru-1.8/GPL3_License.txt %{buildroot}%{_docdir}/%{name}
install -d %{buildroot}%{_sysconfdir}/fonts/conf.d
install -m644 %{SOURCE3} %{buildroot}%{_sysconfdir}/fonts/conf.d

%files
%{_docdir}/%{name}/*
%{fontdir}/*
%{_sysconfdir}/fonts/conf.d/*

%changelog
* Mon May 09 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.04
- Rebuilt for Fedora

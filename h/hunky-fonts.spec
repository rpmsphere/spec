%define         archivename hunkyfonts
%define         fontdir     %{_datadir}/fonts/hunky

Name:           hunky-fonts
Version:        0.3.1
Release:        6.1
Summary:        Modified Bitstream Vera fonts with additional letters
Group:          User Interface/X
License:        Redistributable, with restrictions
URL:            https://sourceforge.net/projects/hunkyfonts/
Source0:        https://download.sourceforge.net/%{archivename}/%{archivename}-%{version}.tar.bz2
BuildArch:      noarch

%description
Free Unicode TrueType fonts for Baltic, Central European, South European
and other languages, including Azeri, Maori, Welsh and Esperanto.

%prep
%setup -q -n %{archivename}-%{version}

%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}%{fontdir}
install -p -m 0644 TTF/*.ttf %{buildroot}%{fontdir}

%clean
rm -rf %{buildroot}

%files
%doc ChangeLog COPYRIGHT.TXT README
%{fontdir}/*.ttf

%changelog
* Tue Mar 31 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.1
- Rebuilt for Fedora
* Wed Dec 30 2009 J. Randall Owens <jrowens@ghiapet.net> - 0.3.1-5
- rebuild for FC11
* Sun Sep 17 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 0.3.1-4
- Rebuild for FE6
- Remove ghosting of %%{fontdir}/fonts.cache-{1,2} for new fontconfig
- Update e-mail address
* Wed Nov  2 2005 Dawid Gajownik <gajownik[AT]gmail.com> - 0.3.1-3
- Add ghosting of %%{fontdir}/fonts.cache-2 (Ville Skyttä)
* Sun Oct 30 2005 Dawid Gajownik <gajownik[AT]gmail.com> - 0.3.1-2
- Correct License and URL tag
* Fri Oct  7 2005 Dawid Gajownik <gajownik[AT]gmail.com> - 0.3.1-1
- New version 0.3.1
* Sun Aug 14 2005 Dawid Gajownik <gajownik[AT]gmail.com> - 0.3.0-1
- Initial RPM release

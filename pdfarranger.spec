Name:           pdfarranger
Version:        1.1
Release:        1
Summary:        PDF file merging, rearranging, and splitting
Group:          Publishing
License:        GPLv3
URL:            https://github.com/jeromerobert/pdfarranger
Source0:        https://github.com/jeromerobert/pdfarranger/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         pdfarranger-1.1-install-appdata-file.patch
Patch1:         pdfarranger-1.1-fix-version.patch
BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-setuptools
BuildRequires:  python3-distutils-extra
BuildRequires:  gettext
BuildRequires:  intltool
Requires:       python3-gobject
Requires:       python3-PyPDF2
Requires:       python3-cairo

%description
PDFArranger is a small python-gtk application, which helps the user
to merge or split pdf documents and rotate, crop and rearrange their
pages using an interactive and intuitive graphical interface.

The tool, which is a graphical front-end for PyPDF2, is a fork of
PDF-Shuffler that aims to "make the project a bit more active".

%prep
%setup -q
%autopatch -p1

%build
%py3_build

%install
python3 setup.py install --root %{buildroot}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README.md TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man1/%{name}.1.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}.ui
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Dec 17 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuild for Fedora
* Sun Dec 16 2018 daviddavid <daviddavid> 1.1-1.mga7
+ Revision: 1341749
- initial package pdfarranger

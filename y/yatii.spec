Name:           yatii
Version:        2.0.0
Release:        4.1
License:        GPLv2+
Summary:        A GUI for creating TikZ/LaTeX formatted figures
URL:            http://code.google.com/p/yatii/
Group:          Productivity/Publishing/TeX/Frontends
Source:         %{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM yatii-remove-shebang.patch badshah400@gmail.com --Remove unnecessary shebang lines from non-executable files
Patch0:         yatii-remove-shebang.patch
BuildRequires:  python2
Requires:       texlive-latex
Requires:       ImageMagick
BuildArch:      noarch

%description
yatii is a graphical user interface for creating TikZ/LaTeX formatted figures

Features:
* Add LaTeX formatted math and text to figures for inclusion in scientific theses and papers.
* Export to eps, pdf, ps, png, jpg and gif formats.

%prep
%setup -q -n %{name}
%patch0 -p1

%build

%install
python2 setup.py install --prefix=%{_prefix} --exec-prefix=%{_exec_prefix} --root=$RPM_BUILD_ROOT

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/yatii
%{_datadir}/yatii
%{python2_sitelib}/Yatii
%{python2_sitelib}/*.py*
%{python2_sitelib}/*.egg-info

%changelog
* Wed May 04 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.0
- Rebuild for Fedora
* Fri Dec 10 2010 badshah400@gmail.com
- Initial package (version 2.0.0)

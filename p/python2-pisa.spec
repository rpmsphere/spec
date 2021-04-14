Name:          python2-pisa
Version:       3.0.33
Release:       10.1
Summary:       PDF generator using HTML and CSS
Group:         System/Libraries/Python
URL:           http://www.xhtml2pdf.com
Source:        http://pypi.python.org/packages/source/p/pisa/pisa-%{version}.tar.gz
Patch:         python-pisa-3.0.33-set.patch
License:       Apache License 2.0
BuildRequires: python2
BuildRequires: python2-setuptools
Requires:      python2-html5lib
Requires:      pyPdf
Requires:      python2-reportlab
BuildArch:     noarch

%description
pisa is a html2pdf converter using the ReportLab Toolkit, the HTML5lib and pyPdf.
It supports HTML 5 and CSS 2.1 (and some of CSS 3).
It is completely written in pure Python so it is platform independent.
The main benefit of this tool that a user with Web skills like HTML and CSS is able to generate PDF templates very quickly without learning new technologies.
Easy integration into Python frameworks like CherryPy, KID Templating, TurboGears, Django, Zope, Plone, Google AppEngine (GAE) etc.

%prep
%setup -q -n pisa-%{version}
%patch -p1

find . -type f -name '._*' -delete

%build
python2 setup.py build

%install
rm -rf "$RPM_BUILD_ROOT"
python2 setup.py install \
   -O1 --skip-build \
   --root="$RPM_BUILD_ROOT" \
   --install-headers=%{_includedir}/python2.7 \
   --install-lib=%{python2_sitelib} \
   --single-version-externally-managed \
   --record=%{name}.filelist

#sed -i "\,\.egg-info/,d;s,.*/man/.*,&.gz," %{name}.filelist
sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf "$RPM_BUILD_ROOT"

%files -f %{name}.filelist
%doc README.txt CHANGELOG.txt LICENSE.txt doc/*.{html,css}

%changelog
* Mon Jun 13 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.33
- Rebuilt for Fedora
* Fri Oct 15 2010 Stefano Cotta Ramusino <stefano.cotta@openmamba.org> 3.0.33-2mamba
- removed useless build requirements
* Tue Oct 12 2010 Stefano Cotta Ramusino <stefano.cotta@openmamba.org> 3.0.33-1mamba
- package created by autospec

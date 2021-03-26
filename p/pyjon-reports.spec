Name:          pyjon-reports
Version:       0.6
Release:       7.1
Summary:       A simple mean of creating templated PDF documents in Python
Group:         System/Libraries/Python
URL:           http://bitbucket.org/jon1012/pyjonreports
Source:        http://pypi.python.org/packages/source/p/pyjon.reports/pyjon.reports-%{version}.tar.gz
License:       MIT
BuildRequires: python2-setuptools
BuildRequires: python2
Requires:      python2-z3c-rml
Requires:      python2-genshi
Requires:      pyPdf
BuildArch:     noarch

%description
Pyjon.Reports is a module bridging z3c.rml, Genshi and pyPdf together to provide a simple mean of creating templated PDF documents in Python.

%prep
%setup -q -n pyjon.reports-%{version}

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install \
   -O1 --skip-build \
   --root=$RPM_BUILD_ROOT \
   --install-headers=%{_includedir}/python2.7 \
   --install-lib=%{python2_sitelib} \
   --single-version-externally-managed \
   --record=%{name}.filelist
#sed -i "\,\.egg-info/,d;s,.*/man/.*,&.gz," %{name}.filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.filelist
%doc README.txt docs/*.txt examples

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuild for Fedora
* Wed Oct 13 2010 Stefano Cotta Ramusino <stefano.cotta@openmamba.org> 0.6-1mamba
- package created by autospec

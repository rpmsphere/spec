%define pyname tappy

Name:           python2-%{pyname}
Version:        0.9.0
Release:        5.1
Summary:        TAPPY is a tidal analysis package
License:        GPL-2
URL:            https://sourceforge.net/projects/tappy/
Group:          Development/Libraries/Python
Source0:        %{pyname}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  python2-devel, python2-setuptools

%description
TAPPY is a tidal analysis package. It breaks down an hourly record of water
levels into the component sine waves. It is written in Python and uses the least
squares optimization and other functions in SciPy. The focus is to make the most
accurate analysis possible. TAPPY only determines the constituents that are
calculatable according to the length of the time series.

%prep
%setup -q -n %{pyname}-%{version}

%build
python2 setup.py build

%install
python2 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT
chmod +x $RPM_BUILD_ROOT/%{python2_sitelib}/%{pyname}_lib/pad/{pad.py,setup_pad.py}
chmod +x $RPM_BUILD_ROOT/%{python2_sitelib}/%{pyname}_lib/{sparser.py,filter.py}
chmod +x $RPM_BUILD_ROOT/%{python2_sitelib}/%{pyname}_lib/pyparsing/setup.py

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{python2_sitelib}/tappy_lib/*.py %{buildroot}%{python2_sitelib}/tappy_lib/*/*.py
sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/tappy.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README AUTHORS COPYING VERSION CHANGES
%{_bindir}/*
%{python2_sitelib}/*

%changelog
* Mon Dec 26 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.0
- Rebuilt for Fedora
* Wed Nov 30 2011 ocefpaf@gmail.com
- Updated to version 0.9.0
  * Added prediction.
  * Added option to create IHOTC standard XML constituent output file to the
    analysis phase. The XML file is what is used for the prediction.
* Sun Mar 20 2011 ocefpaf@yahoo.com.br
- specfile cleanup
* Wed Mar  3 2010 Filipe Fernandes <ocefpaf@gmail.com> - 0.8.3
- first release

%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%define python_version %(%{__python} -c "import sys; print sys.version[:3]")
%undefine _missing_build_ids_terminate_build

Summary: Penpower Handwriting Writepanel by python.
Name: python-penpower
Version: 0.1
Release: 2
License: Commercial
Group: System/Internationalization
Source: %{name}.tar.gz
URL: http://www.penpower.net/
BuildRequires: penpower-devel python-devel swig
Requires: penpower
Obsoletes: penpower-python

%description
Penpower handwriting recognition python API.

%prep
%setup -q -n %{name}
sed -i -e 's/python2\.5/python%{python_version}/g' Makefile README

%build
make

%install
rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{python_sitearch}/penpower

%__cp src/*.so %{buildroot}%{python_sitearch}/
%__cp src/*.py %{buildroot}%{python_sitearch}/

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,root)
%doc example/* README AUTHOR
%{python_sitearch}/*.so
%{python_sitearch}/*.py*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Mon Feb 01 2010 Feather Mountain <john@ossii.com.tw> 0.1-2.ossii
- Fix SPEC

* Thu Apr 17 2009 Feather Mountain <john@ossii.com.tw> 0.1-1.ossii
- Initial package

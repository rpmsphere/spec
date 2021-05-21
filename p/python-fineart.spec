%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%define python_version %(%{__python} -c "import sys; print sys.version[:3]")
%undefine _missing_build_ids_terminate_build

Summary: Fineart Handwriting Writepanel by python.
Name: python-fineart
Version: 0.2
Release: 2
License: Commercial
Group: System/Internationalization
Source: %{name}.tar.gz
URL: http://www.fineart.com.tw
BuildRequires: python-devel, fineart-devel, swig
Requires: fineart

%description
fineart handwriting recognition python API.

%prep
%setup -q -n %{name}
sed -i -e 's/python2\.5/python%{python_version}/g' Makefile README

%build
make

%install
rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{python_sitearch}/fineart

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
- Rebuilt for Fedora
* Mon Feb 01 2010 Feather Mountain <john@ossii.com.tw> 0.2-2.ossii
- Fix SPEC

* Wed Nov 25 2009 Feather Mountain <john@ossii.com.tw> 0.2-1.ossii
- Change wFlag for new version fineart.
- Support standard CJK.

* Tue Nov 17 2009 Feather Mountain <john@ossii.com.tw> 0.1-1.ossii
- Initial package

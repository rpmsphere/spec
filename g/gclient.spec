%define svncheckout 20090601svn72

Name:		gclient
Version:	0.1
Release:	2.%{svncheckout}
Summary:	Wrapper script for getting source code from multiple SCM repositories
Group:		System Environment/Libraries
License:	ASL 2.0
URL:		http://code.google.com/p/gclient/
# No tarballs, pulled from svn
# svn checkout http://gclient.googlecode.com/svn/trunk/ gclient
# cd gclient && rm -rf gclient/.svn/
# tar cvfj ../gclient-20090222svn46.tar.bz2 gclient
Source0:	gclient-%{svncheckout}.tar.bz2
BuildArch:	noarch
Requires:	pymox

%description
The gclient script manages checkouts and updates for a set of client modules 
in various SCM repository locations. The gclient script currently handles 
basic management of one or more Subversion modules, along with their dependent 
modules. Module sources may exist in separate, different Subversion 
repositories.

%prep
%setup -q -n %{name}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -p -m0755 gclient.py %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -s gclient.py gclient
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README.txt
%{_bindir}/gclient*
#%exclude %{_bindir}/gclient.pyc
#%exclude %{_bindir}/gclient.pyo

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Tue Nov 24 2009 Kami <kami@ossii.com.tw> 0.1-2.20090601svn72
- Rebuild for OX 1.5

* Mon Jun  1 2009 Tom "spot" Callaway <tcallawa@redhat.com> 0.1-1.20090601svn72

* Sun Feb 22 2009 Tom "spot" Callaway <tcallawa@redhat.com> 0.1-1.20090222svn46
- Initial package for Fedora

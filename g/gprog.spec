%define _libdir %{_prefix}/lib

Name:				 gprog
Version:			 1.20
Release:			 4.1
Summary:			 GUI Pipe Meter
Source:			 http://stromberg.dnsalias.org/~dstromberg/gprog/releases/gprog-%{version}.tar.gz
Source99:		 %{name}-rpmlintrc
Patch1:			 gprog-fix_paths.patch
URL:				 http://stromberg.dnsalias.org/~dstromberg/gprog/
Group:			 System/X11/Utilities
License:			 GNU General Public License version 3 (GPL v3)
BuildRequires:	 make
Requires:		 python2
BuildArch:		 noarch

%description
gprog is a basic GUI pipe meter that shows the percentage complete as data
moves through a Unix pipe. It is very fast because it uses a dual process
design with a cache oblivious algorithm for self-tuning. Also, the presentation
is largely decoupled from the transfer, so that the GUI won't slow down the
transfer.

%prep
%setup -q -c "%{name}-%{version}"
%patch1
%__sed -i 's|@@LIBDIR@@|%{_libdir}|g' gprog

%build

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__make \
	 prefix="%{_prefix}" \
	 libdir="%{_libdir}" \
	 DESTDIR="$RPM_BUILD_ROOT" \
	 install

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}/usr/lib/%{name}/*.py
sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%doc COPYING README
%{_bindir}/gprog
%{_bindir}/gprog-buf
%{_bindir}/gprog-du-tar
%{_libdir}/gprog

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.20
- Rebuild for Fedora

* Sat Jun 12 2010 pascal.bleser@opensuse.org
- initial package (1.20)

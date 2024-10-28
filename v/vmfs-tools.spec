%undefine _debugsource_packages

Name:               vmfs-tools
Version:            0.2.5
Release:            1
Summary:            Tools to access VMFS file-systems
Source:             https://glandium.org/projects/%{name}/%{name}-%{version}.tar.gz
Patch1:             vmfs-tools-uuid
URL:                https://glandium.org/projects/vmfs-tools/
Group:              System Environment/Base
License:            GPLv2+
BuildRequires:      libuuid-devel 
BuildRequires:      docbook5-style-xsl
BuildRequires:      fuse-devel
BuildRequires:      asciidoc
BuildRequires:      libxslt
BuildRequires:      automake

%description
Originally loosely based on the vmfs code from fluidOps, this set of tools has
since evolved to handle more features from VMFS, such as extents, and allows to
access VMFS through the standard Linux VFS with the help of the FUSE framework.

While it is still work in progress and is not destined for production use yet,
it can be of some help for some people.

%package -n libvmfs-devel
Summary:            Library to access VMFS file-systems
Group:              Development/Libraries

%description -n libvmfs-devel
Originally loosely based on the vmfs code from fluidOps, this set of tools has
since evolved to handle more features from VMFS, such as extents, and allows to
access VMFS through the standard Linux VFS with the help of the FUSE framework.

While it is still work in progress and is not destined for production use yet,
it can be of some help for some people.

%prep
%setup -q
%patch 1 -p1

%build
%configure
make %{?_smp_flags}

%install
%make_install
chmod 0644 "%{buildroot}%{_mandir}/man8"/*.8
install -d "%{buildroot}%{_includedir}/libvmfs"
install -m0644 libvmfs/*.h "%{buildroot}%{_includedir}/libvmfs/"
install -D -m0644 libvmfs/libvmfs.a "%{buildroot}%{_libdir}/libvmfs.a"

%files
%doc AUTHORS LICENSE TODO
%{_sbindir}/debugvmfs
%{_sbindir}/fsck.vmfs
%{_sbindir}/vmfs-fuse
%{_sbindir}/vmfs-lvm
%{_mandir}/man8/*.8*

%files -n libvmfs-devel
%{_includedir}/libvmfs
%{_libdir}/libvmfs.a

%changelog
* Wed May 20 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.5
- Rebuild

* Sat May 26 2012 jengelh@inai.de
- Remove redundant tags/sections from specfile

* Mon May  7 2012 jeffm@suse.com
- Build fixes for libuuid-devel

* Wed Mar 23 2011 pascal.bleser@opensuse.org
- initial version (0.2.1)

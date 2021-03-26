Name:           genext2fs
Summary:        Generate an ext2 filesystem as a normal (non-root) user
License:        GPL-2.0+
Group:          System/Filesystems
Version:        1.4.1
Release:        3.1
URL:            http://genext2fs.sourceforge.net/
Source:         http://downloads.sourceforge.net/%name/%name-%version.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
genext2fs generates an ext2 filesystem as a normal (non-root) user.
It does not require you to mount the image file to copy files on it,
nor does it require that you become the superuser to make device nodes.

%prep
%setup -q

%build
%configure --libdir=/%{_lib}
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING device_table.txt NEWS README TODO 
%{_bindir}/genext2fs
%{_mandir}/man8/genext2fs.8.*

%changelog
* Sun Sep 02 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.1
- Rebuild for Fedora
* Wed Apr 25 2012 Ludwig Nussel <lnussel@suse.de>
- initial version 1.4.1

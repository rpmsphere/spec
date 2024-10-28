%undefine _debugsource_packages
%global pkgname secure_delete

Name:           secure-delete
Version:        3.1
Release:        5
Summary:        Tools to wipe files, free disk space, swap and memory
License:        GPLv1
Group:          System/Base
URL:            https://www.thc.org/
Source0:        https://www.thc.org/download.php?t=r&f=%{pkgname}-%{version}.tar.gz
Patch0:         secure_delete-3.1.mga.diff

%description
Even if you overwrite a file 10+ times, it can still be recovered. This
package contains tools to securely wipe data from files, free disk space,
swap and memory.

%prep
%setup -q -n %{pkgname}-%{version}
%patch 0 -p1

%build
%configure
make

%install
make install \
        INSTALL_DIR=%{buildroot}%{_bindir} \
        MAN_DIR=%{buildroot}%{_mandir} 
install -Dm644 srm.1 %{buildroot}%{_mandir}/man1/sdel.1

%files
%doc CHANGES FILES README *.doc
%{_bindir}/s*
%{_mandir}/man1/*

%changelog
* Sun Jan 01 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 3.1
- Rebuilt for Fedora
* Sun Jan 26 2014 david.david (MLO Team) <david.david> 3.1-3.mga4
+ Rebuild package for Mageia 4 (Core\MLO)
- version: 3.1
* Sun Oct 06 2013 david.david (MLO Team) <david.david> 3.1-2.mga3
+ New revision: 2
- delete srm binary (already exists on repo Mageia)
- add %%Suggests package srm
- rename smem to sdmem to avoid name clash with smem package
- rename and rediff patch0
* Tue Oct 01 2013 Adrien.D (MLO Team) <adrien.d> 3.1-1.mga3
+ Backported from Open Suse
+ Clean "spec" file.

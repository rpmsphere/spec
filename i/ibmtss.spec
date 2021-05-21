Name:           ibmtss
Version:        1.5.0
Release:        1
Summary:        IBM's TPM 2.0 TSS
License:        BSD-3-Clause
Group:          Productivity/Security
URL:            https://sourceforge.net/projects/ibmtpm20tss
Source:         https://sourceforge.net/projects/ibmtpm20tss/files/ibmtss%{version}.tar.gz
Source1:        90-tpm-ibmtss.rules
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  ibmswtpm2
BuildRequires:  openssl-devel
BuildRequires:  libtool

%description
This is a user space TCG Software Stack (TSS) for TPM 2.0. It
implements the functionality equivalent to the TCG TSS working
group's planned ESAPI, SAPI, and TCTI APIs.

It comes with over 100 "TPM tools" that can be used for scripted
apps, rapid prototyping, education, and debugging.

%package devel
Summary:        IBM's TPM 2.0 TSS headers
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Includes IBM's TPM 2.0 TSS C header files.

%prep
%setup -q -c

%build
autoreconf -i
%configure --enable-hwtpm --enable-debug --disable-static
cd utils
%{_libexecdir}/%{name}/tpm_server & tpm_server="$!"
CCFLAGS="%{optflags}" make LNAFLAGS="-Wl,-rpath,%{_libdir}" %{?_smp_mflags}
testfailed=0
TPM_INTERFACE_TYPE=socsim LD_LIBRARY_PATH=.libs ./reg.sh || testfailed=$?
kill "$tpm_server" || :
[ "$testfailed" -eq 0 ]

%install
install -m 644 -D -t %{buildroot}%{_prefix}/lib/udev/rules.d/ %{SOURCE1}
cd utils
%make_install

mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -a policies certificates %{buildroot}/%{_datadir}/%{name}

find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -name .cvsignore | xargs rm -v

%post
%_bindir/udevadm trigger -s tpm -s tpmrm || :

%files
%license LICENSE
%doc ibmtss.doc
%{_bindir}/tss*
%{_mandir}/man1/tss*.1*
%{_libdir}/%{libname}*.so.*
%{_datadir}/%{name}
%{_prefix}/lib/udev/rules.d/*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{libname}*.so

%changelog
* Fri Jun 12 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.0
- Rebuilt for Fedora
* Fri Mar 27 2020 Dominique Leuenberger <dimstar@opensuse.org>
- Don't mess with Epoch: in the long run it can't but cause
  problems. Upstreams that don't understand the meaning of version
  numbers can't be helped with Epoch. Let's rely on the distro
  features for dist-upgrade (that has no problem with a 'version
  downgrade'.
* Mon Mar 23 2020 Michal Suchanek <msuchanek@suse.com>
- Fix dependencies for epoch, remove useless define.
* Fri Jan 31 2020 Michal Suchanek <msuchanek@suse.com>
- Update to upstream version 1.3.0
- copy tpm device permission handling udev rule from tpm2-0-tss
- depend on user(tss) (boo#1162360).
* Sat Aug 24 2019 Jan Engelhardt <jengelh@inai.de>
- Disable static libs (standard openSUSE behavior)
* Wed Aug 14 2019 Michal Suchanek <msuchanek@suse.de>
- Remove installed .cvsignore file
- Don't create already created directory
* Fri Aug  9 2019 Michal Suchanek <msuchanek@suse.com>
- Don't install duplicate headers
* Mon Jul  8 2019 Michal Suchanek <msuchanek@suse.com>
- Remove .la files
* Thu Jul  4 2019 Michal Suchanek <msuchanek@suse.de>
- Update to v1047 (FATE#327307, jsc#SLE-6593, jsc#SLE-9179).
  - now supports autotools
  - supports library versioning
  - installs tools with program prefx
  - remove binary tool wrapper
  - remove makefile.patch
* Tue May 22 2018 msuchanek@suse.com
- Add post/postun ldconfig call
* Fri May 18 2018 jengelh@inai.de
- Fix RPM groups
* Thu May 17 2018 msuchanek@suse.com
- Split off library, spec-clean (bsc#1093612)
* Thu Jan 18 2018 msuchanek@suse.com
- Enable test on BE
* Wed Nov  8 2017 msuchanek@suse.com
- Update to upstream version 1045 - works with OpenSSL 1.1 (bsc#1066914)
* Thu Mar  2 2017 msuchanek@suse.com
- fix description of -devel package
* Wed Mar  1 2017 meissner@suse.com
- update to v755 (FATE#321601)
  - This is the version prefered by IBM.
* Wed Feb  8 2017 jengelh@inai.de
- Wrap description and spell out TSS.
- Move package description up before any build recipes,
  this is the more usual layout.
- Drop unusable "return" command; %%build already executes with
  sh -e.
* Fri Jan 27 2017 msuchanek@suse.com
- Import v713 (FATE#321601)
- Move to libdir and add wrapper script.
- repack source without makefile-beam which has incompatible
  license and is not used in build anyway

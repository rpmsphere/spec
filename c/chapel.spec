Name:           chapel
Version:        1.23.0
Release:        1
License:        BSD
Summary:        An emerging parallel programming language
URL:            http://chapel.cray.com
Group:          Development/Languages
Source:         https://github.com/chapel-lang/chapel/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  bc
BuildRequires:  python3
BuildRequires:  numactl-devel
BuildRequires:  cairo-devel

%description
Chapel supports a multithreaded execution model via high-level abstractions
for data parallelism, task parallelism, concurrency, and nested parallelism.
Chapel's locale type enables users to specify and reason about the placement
of data and tasks on a target architecture in order to tune for locality.
Chapel supports global-view data aggregates with user-defined implementations,
permitting operations on distributed data structures to be expressed in a
natural manner. In contrast to many previous higher-level parallel languages,
Chapel is designed around a multiresolution philosophy, permitting users to
initially write very abstract code and then incrementally add more detail until
they are as close to the machine as their needs require. Chapel supports code
reuse and rapid prototyping via object-oriented design, type inference, and
features for generic programming.

%prep
%setup -q

%build
%make_build

%install
#make_install
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a bin doc lib make modules runtime util %{buildroot}%{_libexecdir}/%{name}
install -Dm644 man/man1/chpl.1 %{buildroot}%{_mandir}/man1/chpl.1

mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/chpl <<EOF
#!/usr/bin/bash
CHPL_HOME=%{_libexecdir}/%{name}
CHPL_HOST_PLATFORM=linux64
export CHPL_HOME CHPL_HOST_PLATFORM
\${CHPL_HOME}/bin/\${CHPL_HOST_PLATFORM}-%{_arch}/chpl "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/chpl

sed -i 's|/usr/bin/env python|/usr/bin/python3|' `find %{buildroot}/usr/libexec/chapel/util -type f`

%files
%doc README* LICENSE* *.md
%{_libexecdir}/%{name}
%{_mandir}/man1/chpl.1.*
%{_bindir}/chpl

%changelog
* Thu Oct 22 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.23.0
- Rebuild for Fedora
* Wed Sep 25 2013 jlinford@paratools.com
- Add module file.
* Wed Sep 25 2013 jlinford@paratools.com
- Initial package.

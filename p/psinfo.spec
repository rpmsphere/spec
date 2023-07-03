Name:               psinfo
Version:            0.12
Release:            3.1
Summary:            Process Information and Statistics
Source:             https://www.ward.nu/computer/psinfo/psinfo-%{version}.tar.gz
Patch1:             psinfo-makefile.patch
URL:                https://www.ward.nu/computer/psinfo/
Group:              System/Monitoring
License:            GPLv2+
BuildRequires:      gcc make glibc-devel

%description
psinfo shows process information and statistics using the kernel /proc
interface. This information includes: process state, environment, arguments and
flags; CPU usage; scheduling; I/O usage; virtual memory status; pagefaults;
capabilities; and signals. psinfo is useful for providing a detailed view of
the current state of an application when diagnosing issues or performance
problems.

%prep
%setup -q
%patch1

%build
%__make %{?jobs:-j%{jobs}} \
    CC="%__cc" \
    OPTFLAGS="%{optflags}" \
    INSTALL="%__install" \
    TARGETDIR="%{_bindir}"

%install
%__make \
    INSTALL="%__install -D" \
    TARGETDIR="%{buildroot}%{_bindir}" \
    install

%files
%doc README
%{_bindir}/psinfo

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.12
- Rebuilt for Fedora
* Fri Jul 23 2010 pascal.bleser@opensuse.org
- initial package (0.12)

Name:                           tscat
Version:                        1.0
Release:                        2.1
Summary:                        Simple Filter that adds Timestamps to Stdin
Source:                 https://www.gerg.ca/software/tscat/tscat-%{version}.tar.gz
URL:                            https://www.gerg.ca/software/tscat/
Group:                  Productivity/Text/Utilities
License:                        MIT/X Consortium License
BuildRequires:  gcc make glibc-devel
BuildRequires:  autoconf automake libtool

%description
tscat is a simple filter that reads a line from standard input, prepends
a timestamp to each line, and writes to standard output. Timestamps can be
absolute (current time of day), relative to process start time, or deltas
since the previous line (previous timestamp).

%prep
%setup -q

%build
%__make \
        %{?jobs:-j%{jobs}} \
        PREFIX="%{_prefix}" \
        BIN_DIR="%{_bindir}" \
        MAN_DIR="%{_mandir}/man1" \
        CFLAGS="%{optflags}"

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__install -D -m 0755 tscat "$RPM_BUILD_ROOT%{_bindir}/tscat"
%__install -D -m 0644 tscat.1 "$RPM_BUILD_ROOT%{_mandir}/man1/tscat.1"

%files
%doc README
%{_bindir}/tscat
%doc %{_mandir}/man1/tscat.1*

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora

* Sat Dec 29 2007 Pascal Bleser <guru@unixtech.be> 1.0
- new package

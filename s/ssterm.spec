Name:               ssterm
Version:            1.2
Release:            3.1
Summary:            Simple Serial-Port Terminal
Source:             https://github.com/downloads/vsergeev/ssterm/ssterm-%{version}.tar.gz
Patch1:             ssterm-optflags.patch
URL:                https://dev.frozeneskimo.com/software_projects:ssterm
Group:              Applications/Communications
License:            GNU General Public License version 2 or later (GPL v2 or later)
BuildRequires:      ncurses-devel
BuildRequires:      gcc make glibc-devel

%description
ssterm (short for "simple serial-port terminal") is a console-based serial port
terminal with curses and stdin/stdout user interfaces. ssterm supports a
variety of features, such as hexadecimal data representation, remapping of
transmitted and received newlines, newline character color-coding, buffer
scrolling/dumping, and data piping.

%prep
%setup -q
%patch 1

%build
%__make %{?jobs:-j%{jobs}} \
    CC="%__cc" \
    OPTFLAGS="%{optflags}" \
    BINDIR="%{_bindir}"

%install
%__install -d %{buildroot}%{_bindir}
%__make \
    BINDIR=%{buildroot}%{_bindir} \
    install

%files
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/ssterm

%changelog
* Sun May 26 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2
- Rebuilt for Fedora
* Tue Feb  8 2011 pascal.bleser@opensuse.org
- initial version (1.2)

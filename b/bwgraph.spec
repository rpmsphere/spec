Name:           bwgraph
Version:        1
Release:        5.1
License:        LGPL
Source:         bwgraph.tar.bz2
Group:          Development/Tools
Summary:        Bandwidth graph on the kernel.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
C code creates a postscript file that is fed to ghostscript
to create a pnm file that is scaled to 50% with pnmscale to
antialias and then converted to png by pnmtopng, and the original
postscript output file is converted to pdf by ghostscript's
ps2pdf14.

You'll need ghostscript installed in addition to netpbm for
the other tools. Ghostscript itself could have been used to
create a png, but the output file was much larger and the
resulting image was not as visually appealing.

%prep
%setup -q -n bwgraph

%build
gcc %{optflags} -o bw bw.c

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 bw $RPM_BUILD_ROOT%{_bindir}/bw

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_bindir}/bw

%changelog
* Fri Jun 22 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1
- Rebuilt for Fedora

* Sat Oct 03 2009 doiggl@velocitynet.com.au
- packaged bwgraph version 1 using the buildservice spec file wizard

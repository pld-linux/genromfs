Summary:	Tool for creating romfs filesystems
Name:		genromfs
Version:	0.3
Release:	4
License:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	ftp://ftp.banki.hu/pub/linux/local/%{name}-%{version}.tar.gz
Patch0:		genromfs-0.3.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveOS:	Linux

%description
Genromfs is a tool for creating romfs filesystems, which are
lightweight, read-only filesystems supported by the Linux kernel.

%description -l pl
genromfs jest narzêdziem s³u¿±cym do tworzenia systemów plików romfs,
które s± lekkimi systemami plików tylko do odczytu, obs³ugiwanymi
przez j±dro Linuksa.

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

make install PREFIX=$RPM_BUILD_ROOT
strip $RPM_BUILD_ROOT%{_bindir}/genromfs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*

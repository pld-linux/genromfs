Summary: Tool for creating romfs filesystems.
Name: genromfs
Version: 0.3
Release: 4
Copyright: GPL
Group: System Environment/Base
Source: ftp://ftp.banki.hu/pub/linux/local/genromfs-0.3.tar.gz
Patch: genromfs-0.3.patch
BuildRoot: /var/tmp/%{name}-root
ExclusiveOS: Linux

%description
Genromfs is a tool for creating romfs filesystems, which are
lightweight, read-only filesystems supported by the Linux
kernel.

%description -l pl
genromfs jest narzêdziem s³u¿±cym do tworzenia systemów plików romfs, które
s± lekkimi systemami plików tylko do odczytu, obs³ugiwanymi przez j±dro Linuksa.

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
make install PREFIX=$RPM_BUILD_ROOT
strip $RPM_BUILD_ROOT/usr/bin/genromfs

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/*
/usr/man/man8/*

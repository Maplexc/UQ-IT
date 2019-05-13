class Disk(object):
    """ disk of the game """
    def __init__(self, disk_id, color):
        """ constract a disk with disk_id and color

            Parameters:
                disk_id (int): id of disk (disk with smaller id is larger)
                color (str): color of disk """
        self._id = disk_id
        self._color = color
        self._rod = 0
        self._num_in_rod = 0
        self._is_active = False
        self.move = False

    def set_rod(self, rodnum):
        """ set the rod num of that disk """
        self._rod = rodnum

    def set_num_in_rod(self, num):
        """ set the total num of disks in the rod """
        self._num_in_rod = num

    def get_rod(self):
        """ get the rod num of that disk """
        return self._rod

    def get_num_in_rod(self):
        """ return the total num of disks in the rod """
        return self._num_in_rod            

    def get_id(self):
        """ return the id of disk"""
        return self._id

    def set_active(self):
        """ set active state to True """
        self._is_active = True

    def set_active_off(self):
        """ set active state to False """
        self._is_active = False
        
    def __str__(self):
        """ return the string representation of the disk """
        return 'disk'+str(self._id)

    def __repr__(self):
        """ return the string representation of the disk """
        return self.__str__()


class Rod(object):
    """ rod of the game """
    def __init__(self, rod_id): 
        """ constract a rod with rod_id

            Parameter:
                rod_id (int): id of the rod"""
        self._id = rod_id        
        self._disks = []

    def get_id(self):
        """ return id of rod """
        return self._id

    def get_disks(self):
        """ return disks in the rod """
        return self._disks

    def get_num_of_disks(self):
        """ return the num of disks in the rod """
        return len(self._disks)

    def get_top(self):
        """ return the top disk """
        if len(self._disks) > 0:
            return self._disks[-1]
        return None
        
    def add_disk(self, disk):
        """ add a disk to list
            return False if disk is not allow to move to that rod

            Parameter:
                disk (Disk)"""
        if disk == None:
            return
        if len(self._disks) == 0:        
            disk.set_rod(self._id)
            self._disks.append(disk)
            self._disks[-1].set_num_in_rod(len(self._disks))
            return True
        elif disk.get_id() > self._disks[-1].get_id():
            self._disks[-1].set_active_off()
            disk.set_active()
            disk.set_rod(self._id)
            self._disks.append(disk)
            self._disks[-1].set_num_in_rod(len(self._disks))
            return True
        else:
            return False

    def remove_disk(self, disk):
        """ remove the last disk in rod """
        self._disks.remove(disk)
        if len(self._disks) > 0:
            self._disks[-1].set_active()
    
        
        

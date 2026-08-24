class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        0,1,0,3,12
        1,0,0,3,12
        1,0,3,0,12
        1,3,0,0,12
        1,3,0,12,0
        1,3,12,0,0

        0を右に持っていくのではなく、
        0以外を左に持っていく？
        いや、どんどん右に進んでいって、もし0ではない場合は、
        左に移動するのか。
        左に移動していく過程で、
        もし0ではないものと比較した、または
        もし先頭になった場合は、右に進み直す。
        そもそもin placeだけってどうやるんだ？

        そうか空間O(1)であれば。
        インデックス変数idx :intを宣言し、
        最後に0だった位置を記憶させて、
        もし0以外の数値nums[i]とiで出会った場合は、
        最後に0だった位置nums[idx]に当該数値nums[i]を代入し、
        nums[i]=0にして、
        変数位置idx = idx + 1して記憶させ、
        これを最後まで繰り返し、
        iが最後まで行ったらbreak.
        """
        idx :int = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx] = nums[i]
                nums[i] = 0
                idx = idx + 1
